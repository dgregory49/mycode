#!/usr/bin/env python3

import uuid

try:
    howMany = int(input("How many UUIDs should be generated? "))

    print("Generating UUIDs...")

    for rando in range(howMany):
        print(uuid.uuid4())
except:
    print("You must enter a number.")
