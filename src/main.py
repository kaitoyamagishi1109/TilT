#imports
import json
import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from datetime import datetime, timedelta, timezone

#variable initializations
US_Eastern = timezone(timedelta(hours=-4), 'US/Eastern')
timenow = datetime.now(US_Eastern)

#class initialization
class Vehicles:
    def __init__(self, direction_id, timetil, vehicle_id, current_status = "", stop = ""):
        self.direction_id = direction_id
        self.timetil = timetil
        self.vehicle_id = vehicle_id
        #under this comment are attributes added to the object from the oher API response
        self.current_status = current_status
        self.stop = stop

#first function: recieves station ID, returns array of Vehicles with direction ID, minutes til arrival, and vehicle ID
def findVehicles(event,context):
    #get rid of header slash
    path = event["path"][1:]
    #fetch station IDs from lambda API call path
    path = path.split('/')
    userstops = path[2] + "%2C" + path[3]
    #call MBTA API using the path
    predictions = requests.get("https://api-v3.mbta.com/predictions?sort=arrival_time&filter%5Bstop%5D=" + userstops).json()
    myVehicles = []
    #counts of vehicles heading in each direction
    toBC = 0
    toPS = 0
    #if whatever happens and API fails to recieve 
    if not predictions["data"]:
        return False
    #we fetch a maximum of 4 vehicles in the list
    while (len(myVehicles) < 4):
        for i in (predictions["data"]):
            #if direction is 0 (to BC), vehicle data is present and there is less than 2 vehicle data for this direction
            if ((i["attributes"]["direction_id"] == 0) and (i["relationships"]["vehicle"]["data"] != None) and (toBC < 2)):
                #block of code to get the time until the next vehicle
                timetil0 = i["attributes"]["arrival_time"]
                datetime0 = datetime.strptime(timetil0, "%Y-%m-%dT%H:%M:%S-04:00")
                et_datetime0 = datetime0.replace(tzinfo=US_Eastern)
                mintilarrival0 = round((abs(et_datetime0-timenow).total_seconds())/60)
                #Create a new object with the direction id, minutes until arrival and the vehicle id
                myVehicles.append(Vehicles(0,mintilarrival0,i["relationships"]["vehicle"]["data"]["id"]))
                toBC += 1
            #if direction is 1 (to park street), vehicle data is present and there is less than 2 vehicle data for this direction
            elif ((i["attributes"]["direction_id"] == 1) and (i["relationships"]["vehicle"]["data"] != None) and (toPS < 2)):
                #block of code to get the time until the next vehicle
                timetil1 = i["attributes"]["arrival_time"]
                datetime1 = datetime.strptime(timetil1, "%Y-%m-%dT%H:%M:%S-04:00")
                et_datetime1 = datetime1.replace(tzinfo=US_Eastern)
                mintilarrival1 = round((et_datetime1-timenow).total_seconds()/60)
                #Create a new object with the direction id, minutes until arrival and the vehicle id
                myVehicles.append(Vehicles(1,mintilarrival1,i["relationships"]["vehicle"]["data"]["id"]))
                toPS += 1
            #if there is no vehicles id
            elif (i["relationships"]["vehicle"]["data"] == None):
                timetil2 = i["attributes"]["arrival_time"]
                datetime2 = datetime.strptime(timetil2, "%Y-%m-%dT%H:%M:%S-04:00")
                et_datetime2 = datetime2.replace(tzinfo=US_Eastern)
                mintilarrival2 = round((et_datetime2-timenow).total_seconds()/60)
                #print minutes til arrival for reference
                myVehicles.append(Vehicles(i["attributes"]["direction_id"],mintilarrival2,"NoID"))
            #safety catch (usually gets trapped here since train is missing vehicle ID)
            else:
                break
        #if the whole API response gets iterated but doesn't reach 4 vehicles, break
        break
    
    return myVehicles
    
#second function: recieves list of vehicles, passes their vehicle ID to second API to recieve current status and station theyre
#approaching towards
def findStatus(myVehicles):
    #string of vehicle ids to pass to api
    vehicleslist = ""
    index = 0
    #Iterate through the vehicle object list and concatinate vehicle name, now ready to pass to the API
    for i in myVehicles:
        vehicleslist += (i.vehicle_id+"%2C")

    #call vehicles API to fetch vehicle data
    vehiclesdata = requests.get("https://api-v3.mbta.com/vehicles?filter%5Bid%5D=" + vehicleslist).json()
    for j in (vehiclesdata["data"]):
        #register attributes current_status and stop
        myVehicles[index].current_status = j["attributes"]["current_status"]
        myVehicles[index].stop = j["relationships"]["stop"]["data"]["id"]
        index += 1
    return myVehicles

def lambda_handler(event, context):
    #initialize response from the whole function
    VehiclesJson = []
    #get rid of header slash
    path = event["path"][1:]
    #fetch station IDs from lambda API call path
    stops = path.split('/')
    #if there is any vehicle present(first function returns true)
    if event["path"] == "/":
        VehiclesJson = "Path not provided."
    else:
        myVehicles = findVehicles(event, context)
        if not myVehicles:
            VehiclesString = "No Vehicles Data"
        else:
            #call second function
            VehiclesInfo = findStatus(myVehicles)
            #append response from 2 functions to the new list (convert objects to list of json)
            for i in VehiclesInfo:
                VehiclesJson.append(json.dumps(i.__dict__))
            #IMPORTANT: JSON dumps the JSON dumped list of strings
            VehiclesString = json.dumps(VehiclesJson)
    
    #return default lines and list of approaching vehicles as body(json)
    return {
        "isBase64Encoded": "true",
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": VehiclesString
    }