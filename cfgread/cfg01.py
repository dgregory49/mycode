#!/usr/bin/env python3

with open("vlanconfig.cfg", "r") as configfile:
    print(configfile.read())
    
with open("vlanconfig.cfg", "r") as configfile:    
    configlist = configfile.readlines()
    print(configlist)
    
    for x in configlist:
        print(x)
