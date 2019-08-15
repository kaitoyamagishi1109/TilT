#imports
import requests
from datetime import datetime
from pytz import timezone

#variable initializations
toBC = 0
toPS = 0
vehicleNum = 0
timenow = datetime.now(timezone("US/Eastern"))
vehicles = []
myVehicles = []
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
    def __init__(self, direction_id, current_status, stop):
        self.direction_id = direction_id
        self.current_status = current_status
        self.stop = stop

#API call
predictions = requests.get("https://api-v3.mbta.com/predictions?sort=arrival_time&filter%5Bstop%5D=70145%2C70144").json()

#Iterate through response from predictions API: Find two train IDs of closest trains and put them into list "vehicles"
while (len(vehicles) < 4):
    for i in (predictions["data"]):
        if ((i["attributes"]["direction_id"] == 0) and (i["relationships"]["vehicle"]["data"] != None) and (toBC < 2)):
            vehicles.append(i["relationships"]["vehicle"]["data"]["id"])
            #block of code to get the time until the next vehicle
            timetil0 = i["attributes"]["arrival_time"]
            datetime0 = datetime.strptime(timetil0, "%Y-%m-%dT%H:%M:%S%z")
            mintilarrival0 = round((abs(datetime0-timenow).total_seconds())/60)
            print("Next train headed to Boston College arriving in " + str(mintilarrival0) + " minutes.")
            toBC += 1
        elif ((i["attributes"]["direction_id"] == 1) and (i["relationships"]["vehicle"]["data"] != None) and (toPS < 2)):
            vehicles.append(i["relationships"]["vehicle"]["data"]["id"])
            #block of code to get the time until the next vehicle
            timetil1 = i["attributes"]["arrival_time"]
            datetime1 = datetime.strptime(timetil1, "%Y-%m-%dT%H:%M:%S%z")
            mintilarrival1 = round((abs(datetime1-timenow).total_seconds())/60)
            print("Next train to headed Park Street arriving in " + str(mintilarrival1) + " minutes.")
            toPS += 1
        else:
            break

#concatinate the items in the list "vehicles" in a format specified by the API call
vehicleslist = "%2C".join(vehicles)
#call vehicles API to fetch vehicle data
vehiclesdata = requests.get("https://api-v3.mbta.com/vehicles?sort=direction_id&filter%5Bid%5D=" + vehicleslist).json()
for j in (vehiclesdata["data"]):
    stopid = j["relationships"]["stop"]["data"]["id"]
    myVehicles.append(Vehicles(j["attributes"]["direction_id"],j["attributes"]["current_status"],stops[stopid]))
    vehicleNum += 1

for k in myVehicles:
    print(k.direction_id)
    print(k.current_status)
    print(k.stop)
    print()