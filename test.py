#imports
import requests

#API requests
request = requests.get("https://api-v3.mbta.com/stops/70148")
#print(request.text)

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
    "Boston University Central" :   {0 : 70110, 1 : 70110},
    "Boston University East" :      {0 : 70110, 1 : 70110},
    "Blandford Street" :            {0 : 70110, 1 : 70110},
    "Kenmore" :                     {0 : 70110, 1 : 70110},
    "Hynes Convention Center" :     {0 : 70110, 1 : 70110},
    "Copley" :                      {0 : 70110, 1 : 70110},
    "Arlington" :                   {0 : 70110, 1 : 70110},
    "Boylston" :                    {0 : 70110, 1 : 70110},
    "Park Street" :                 {0 : 70110, 1 : 70110}
}

#print(stops["Boston College"][0])

#for key, value in stops.items():
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


for prev,item,next in neighborhood(stops.items()):
    print (prev, item, next)