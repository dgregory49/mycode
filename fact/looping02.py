#!/usr/bin/env python3

dnsFile = open("dnsservers.txt", "r")

dnsList = dnsFile.readlines()

for svr in dnsList:
    print(svr, end="")

dnsFile.close()
