#!/usr/bin/env python3

switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

print(switch["hostname"])
print(switch["ip"])

#print(switch["lynx"])

print("First test: ")
print(switch.get("lynx"))

print("Second test: ")
print(switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!"))

print("Third test: ")
print(switch.get("version"))

print("Fourth test: ")
print(switch.keys())

print("Fifth test: ")
print(switch.values())

print("Sixth test: ")
switch.pop("version")
print(switch.keys())
print(switch.values())

print("Seventh test: ")
switch["adminlogin"] = "karl08"
print(switch.keys())
print(switch.values())

print("Eighth test: ")
switch["password"] = "qwerty"
print(switch.keys())
print(switch.values())
