#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def getMacAddress(address): return(netifaces.ifaddresses(address)[netifaces.AF_LINK][0]['addr'])
def getIpAddress(address): return(netifaces.ifaddresses(address)[netifaces.AF_INET][0]['addr'])

def main():
    """ Print details of network interfaces """
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print("MAC:", getMacAddress(i))
            print("IP:", getIpAddress(i))
        except:
            print('Could not collect adapter information')

main()
