#imports
import requests
from datetime import datetime
from pytz import timezone

predictions = requests.get("https://api-v3.mbta.com/predictions?sort=arrival_time&filter%5Bstop%5D=70145%2C70144").json()

toBC = 0
toPS = 0

timenow = datetime.now(timezone("US/Eastern"))

vehicles = []

#Iterate through response from predictions API: Find two train IDs of closest trains and put them into vehicles list
for i in (predictions["data"]):
    if (toBC < 1) or (toPS < 1):
        if (i["attributes"]["direction_id"] == 0):
            vehicles.append(i["relationships"]["vehicle"]["data"]["id"])
            timetil0 = i["attributes"]["arrival_time"]
            datetime0 = datetime.strptime(timetil0, "%Y-%m-%dT%H:%M:%S%z")
            mintilarrival0 = round((abs(datetime0-timenow).total_seconds())/60)
            print("Next train to Boston College arriving in " + str(mintilarrival0))
            toBC += 1
        elif (i["attributes"]["direction_id"] == 1):
            vehicles.append(i["relationships"]["vehicle"]["data"]["id"])
            timetil1 = i["attributes"]["arrival_time"]
            datetime1 = datetime.strptime(timetil1, "%Y-%m-%dT%H:%M:%S%z")
            mintilarrival1 = round((abs(datetime1-timenow).total_seconds())/60)
            print("Next train to Park Street arriving in " + str(mintilarrival1))
            toPS += 1

print(vehicles)