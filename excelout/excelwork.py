#!/usr/bin/env python3

import pyexcel

# Request data from user
def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_port = input("What is the port number: ")
    input_desc = input("Description for this IP: ")
    d = {"IP": input_ip, "driver": input_driver, "port": input_port, "description": input_desc}
    return d

mylistdict = []

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or \
    enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

try:
    pyexcel.save_as(records=mylistdict, dest_file_name=f'/home/student/static/{filename}.xls')
    print("The file " + filename + ".xls should be in your local directory")
except:
    print("Unable to save file. Please try again.")
