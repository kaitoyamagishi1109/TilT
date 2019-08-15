#Copyright 2019, Kaito Yamagishi, all rights reserved

#imports
import requests
from datetime import datetime
from pytz import timezone

#Dictionary of stop names corresponding to their stop IDs based on direction of trip
stops = {
    #0 is heading to Boston College, 1 is heading to Park Street
    "Boston College" :              {0 : 70107, 1 : 70106},
    "South Street" :                {0 : 70111, 1 : 70110},
    "Chestnut Hill Avenue" :        {0 : 70113, 1 : 70112},
    "Chiswick Road" :               {0 : 70115, 1 : 70114},
    "Sutherland Road" :             {0 : 70117, 1 : 70116},
    "Washington Street" :           {0 : 70121, 1 : 70120},
    "Warren Street" :               {0 : 70125, 1 : 70124},
    "Allston Street" :              {0 : 70127, 1 : 70126},
    "Griggs Street" :               {0 : 70129, 1 : 70128},
    "Harvard Avenue" :              {0 : 70131, 1 : 70130},
    "Packards Corner" :             {0 : 70135, 1 : 70134},
    "Babcock Street" :              {0 : 70137, 1 : 70136},
    "Pleasant Street" :             {0 : 70139, 1 : 70138},
    "Boston University West" :      {0 : 70143, 1 : 70142},
    "Boston University Central" :   {0 : 70145, 1 : 70144},
    "Boston University East" :      {0 : 70147, 1 : 70146},
    "Blandford Street" :            {0 : 70149, 1 : 70148},
    "Kenmore" :                     {0 : 71151, 1 : 70150},
    "Hynes Convention Center" :     {0 : 70153, 1 : 70152},
    "Copley" :                      {0 : 70155, 1 : 70154},
    "Arlington" :                   {0 : 70157, 1 : 70156},
    "Boylston" :                    {0 : 70159, 1 : 70158},
    "Park Street" :                 {0 : 70196, 1 : 71199}
}

            
#Class definition
class Vehicle:
    def __init__(self, vehicle_id, direction_id, status = "", station_id = ""):
        self.vehicle_id = vehicle_id
        self.direction_id = direction_id
        self.status = status
        self.station_id = station_id

    def getstatus(self):
        vehicledata = requests.get("https://api-v3.mbta.com/vehicles/" + self.vehicle_id).json()
        #self.status = vehicledata["data"]["attributes"]["current_status"]
        #self.station_id = vehicledata["data"]["stop"]["data"]["id"]
        self.status = "INCOMING_AT"
        self.station_id = "70145"
        return self.status, self.station_id

# def mintil(stopids):
#     closeststa = ["70147","70146"]
#     #Requests predictions for the next 3 trains approaching stop from PARK STREET to BC
#     predictionsPtoB = requests.get("https://api-v3.mbta.com/predictions?page%5Blimit%5D=3&sort=arrival_time&filter%5Bstop%5D=" + closeststa[0]).json()
#     #equests predictions for the next 3 trains approaching stop from BC to PARK STREET
#     predictionsBtoP = requests.get("https://api-v3.mbta.com/predictions?page%5Blimit%5D=3&sort=arrival_time&filter%5Bstop%5D=" + closeststa[1]).json()

#     #Calculate mins until the next train PtoB (If 0, show next)
#     def timetilPtoB(index):
#         #Take the arrival time of the next train from the json API response
#         nexttrain = predictionsPtoB["data"][index]["attributes"]["arrival_time"]
#         #Convert time to datetime type and add timezone
#         nexttrain_datetime = datetime.strptime(nexttrain, "%Y-%m-%dT%H:%M:%S%z")
#         timenow = datetime.now(timezone("US/Eastern"))
#         #Get deltatime value by subtracting current time from arrival time
#         mintilarrival = ((abs(nexttrain_datetime-timenow).total_seconds())/60)
#         roundedmin = round(mintilarrival)
#         #If the train is coming in less than a minute, take arriving time of next train
#         if roundedmin == 0:
#             #via recursion, incrementing the index of the json API response
#             roundedmin = timetilPtoB(index+1)
#         return roundedmin

#     #Calculate mins until the next train BtoP (If 0, show next)
#     def timetilBtoP(index):
#         #Take the arrival time of the next train from the json API response
#         nexttrain = predictionsBtoP["data"][index]["attributes"]["arrival_time"]
#         #Convert time to datetime type and add timezone
#         nexttrain_datetime = datetime.strptime(nexttrain, "%Y-%m-%dT%H:%M:%S%z")
#         timenow = datetime.now(timezone("US/Eastern"))
#         #Get deltatime value by subtracting current time from arrival time
#         mintilarrival = ((abs(nexttrain_datetime-timenow).total_seconds())/60)
#         roundedmin = round(mintilarrival)
#         #If the train is coming in less than a minute, take arriving time of next train
#         if roundedmin == 0:
#             #via recursion, incrementing the index of the json API response
#             roundedmin = timetilBtoP(index+1)
#         return roundedmin

#     #return trainids and the minutes until next train
#     mins = [timetilPtoB(0),timetilBtoP(0)]
#     return mins


def main():
    trains = []
    closeststa = ["70147","70146"]
    vehiclesPtoB = requests.get("https://api-v3.mbta.com/predictions?page%5Blimit%5D=3&sort=arrival_time&filter%5Bstop%5D=" + closeststa[0]).json()
    for i in range(3):
        #vehicle_id = vehiclesPtoB["data"][i]["vehicle"]["id"]
        #direction_id = vehiclesPtoB["data"][i]["attributes"]["direciton_id"]
        vehicle_id = "G-10251"
        direction_id = 0
        strName = "toBC"+str(i)
        strName = Vehicle(vehicle_id, direction_id)
        trains.append(strName)
        strName.getstatus()
        trains.append(strName)

    vehiclesBtoP = requests.get("https://api-v3.mbta.com/predictions?page%5Blimit%5D=3&sort=arrival_time&filter%5Bstop%5D=" + closeststa[1]).json()
    for j in range(3):
        #vehicle_id = vehiclesBtoP["data"][i]["vehicle"]["id"]
        #direction_id = vehiclesBtoP["data"][i]["attributes"]["direciton_id"]
        vehicle_id = "G-10252"
        direction_id = 1
        strName = "toPS"+str(j+3)
        strName = Vehicle(vehicle_id, direction_id)
        strName.getstatus()
        trains.append(strName)


if __name__ == '__main__':
        # mins = mintil(stopids)
        # print("Next train heading East towards Boston College is arriving in %d minutes."%mins[0])
        # print("Next train heading West towards Park Steet is arriving in %d minutes."%mins[1])
        main()