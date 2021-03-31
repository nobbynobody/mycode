#!/usr/bin/env python3
## create file object in "r"ead mode
linecount = 0

vlanfile = input("Input name of vlanfile: ")
if (vlanfile == ""):
    vlanfile = "vlanconfig.cfg"

with open(vlanfile, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    linecount = len(configlist)
    #linecount +=1
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print("Number of lines: " + str(linecount))


