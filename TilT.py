#Copyright 2019, Kaito Yamagishi, all rights reserved

#imports
import requests

#API requests
request = requests.get("https://api-v3.mbta.com/stops/70148")
#print(request.text)

#Dictionary of stop names corresponding to their stop IDs based on direction of trip
stopids = {
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
    "Park Street" :                 {0 : 71199, 1 : 70196}
}

print(stopids["Boston University East"])

for key, value in stopids.items():
    #print(value[0])

#Markus Jarderot, https://stackoverflow.com/questions/323750/how-to-access-previous-next-element-while-for-looping/22030004
def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)


for prev,item,next in neighborhood(stopids.items()):
    #print (prev, item, next)