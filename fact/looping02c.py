#!/usr/bin/env python3

with open("dnsservers.txt", "r") as dnsFile:

    for svr in dnsFile:
        print(svr, end="")
