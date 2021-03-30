#!/usr/bin/env python3

# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across farms list elements
for x in farms:
    farmname = x.get("name")
    print("Farmname: " + farmname, " | Agriculture: ", end=" ")
    for y in x.get("agriculture"):
        print (y, end=", ")
    print("\n")







#print(farms[0].get("name")
#print(farms[0].get("name"))
#print(farms[0].get("agriculture"))
#for x in (farms[0].get("agriculture"))
#for x in (farms[0].get("agriculture")):
#        print(x)
#for x in (farms[0].get("agriculture")):
#        print(x, end=" ")
