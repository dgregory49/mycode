#!/usr/bin/env python3

fileName = input("Enter name of configuration file: ")

with open(fileName, "r") as configfile:
    configlist = configfile.readlines()

    print(configlist, "\nNumber of lines in file:", len(configlist))
