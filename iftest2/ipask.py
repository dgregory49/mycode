#!/usr/bin/env python3

import ipaddress

ipchk = input("Enter an IP Address: ")

if ipchk == "192.168.70.1":
    print(f"WARNING: IP Address is set to the gateway: {ipchk}. This is not recommended.")
elif ipchk:
    try:
        ipaddress.ip_address(ipchk)
        print("IP Address is set: " + ipchk)
    except:
        print("Invalid IP Address")
else:
    print("You did not provide an IP Address")
