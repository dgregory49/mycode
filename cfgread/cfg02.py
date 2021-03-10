#!/usr/bin/env python3

with open("vlanconfig.cfg", "r") as configfile:
    configblog = configfile.read()

    configlist = configblog.splitlines()

    print(configlist)
