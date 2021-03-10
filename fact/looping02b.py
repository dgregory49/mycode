#!/usr/bin/env python3

with open("dnsservers.txt", "r") as dnsFile:

    dnsList = dnsFile.readlines()

    for svr in dnsList:
        print(svr, end="")
