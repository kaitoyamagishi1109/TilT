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
#dict containing all stop ids for stop names
stops = {
    #direction_id = 0, headed to boston college
    "70107" : "Boston College",
    "70111" : "South Street",
    "70113" : "Chestnut Hill Avenue",
    "70115" : "Chiswick Road",
    "70117" : "Sutherland Road",
    "70121" : "Washington Street",
    "70125" : "Warren Street",
    "70127" : "Allston Street",
    "70129" : "Griggs Street",
    "70131" : "Harvard Avenue",
    "70135" : "Packards Corner",
    "70137" : "Babcock Street",
    "70139" : "Pleasant Street",
    "70141" : "Saint Paul Street",
    "70143" : "Boston University West",
    "70145" : "Boston University Central",
    "70147" : "Boston University East",
    "70149" : "Blandford Street",
    "71151" : "Kenmore",
    "70153" : "Hynes Convention Center",
    "70155" : "Copley",
    "70157" : "Arlington",
    "70159" : "Boylston",
    "70196" : "Park Street",
    #direction_id = 1, headed to park street
    "70106" : "Boston College",
    "70110" : "South Street",
    "70112" : "Chestnut Hill Avenue",
    "70114" : "Chiswick Road",
    "70116" : "Sutherland Road",
    "70120" : "Washington Street",
    "70124" : "Warren Street",
    "70126" : "Allston Street",
    "70128" : "Griggs Street",
    "70130" : "Harvard Avenue",
    "70134" : "Packards Corner",
    "70136" : "Babcock Street",
    "70138" : "Pleasant Street",
    "70140" : "Saint Paul Street",
    "70142" : "Boston University West",
    "70144" : "Boston University Central",
    "70146" : "Boston University East",
    "70148" : "Blandford Street",
    "70150" : "Kenmore",
    "70152" : "Hynes Convention Center",
    "70154" : "Copley",
    "70156" : "Arlington",
    "70158" : "Boylston",
    "70199" : "Park Street"
}

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
    userstops = event["path"]
    userstops = userstops[1:]
    predictions = requests.get("https://api-v3.mbta.com/predictions?sort=arrival_time&filter%5Bstop%5D=" + userstops).json()
    myVehicles = []
    toBC = 0
    toPS = 0
    if not predictions["data"]:
        print("Vehicle Data is Empty")
        return False
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
            elif (i["relationships"]["vehicle"]["data"] == None):
                timetil2 = i["attributes"]["arrival_time"]
                datetime2 = datetime.strptime(timetil2, "%Y-%m-%dT%H:%M:%S-04:00")
                et_datetime2 = datetime2.replace(tzinfo=US_Eastern)
                mintilarrival2 = round((et_datetime2-timenow).total_seconds()/60)
                print("Vehicle without an ID is arriving in " + str(mintilarrival2) + " minutes.\n")
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
        stopid = j["relationships"]["stop"]["data"]["id"]
        myVehicles[index].stop = stops[stopid]
        index += 1
    return myVehicles

def lambda_handler(event, context):
    #initialize response from the function
    VehiclesJson = []
    #if there is any vehicle present(first function returns true)
    if findVehicles(event, context):
        myVehicles = findVehicles(event, context)
        #call second function
        VehiclesInfo = findStatus(myVehicles)
        #append response from 2 functions to the new list (convert objects to list of json)
        for i in VehiclesInfo:
            VehiclesJson.append(json.dumps(i.__dict__))
    else:
        VehiclesJson = "False"
    
    #return default lines and list of approaching vehicles as body(json)
    return {
        "isBase64Encoded": "true",
        "statusCode": 200,
        "headers": {},
        "body": VehiclesJson
    }
