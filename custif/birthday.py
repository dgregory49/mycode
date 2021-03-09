#!/usr/bin/env python3

from holidays import holidays

MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

month = input("Enter your birth month: ")
shortMonth = month[:3].lower()

if shortMonth in MONTHS:

    try:
        day = int(input(f"Which day in {month} were you born? "))
        formattedDay = str(day).zfill(2)
        formattedDate = f"{formattedDay}-{shortMonth}"

        holiday=holidays.get(formattedDate)

        if holiday == None:
            print(f"I'm sorry. {formattedDate} is not a holiday.")
        else:
            print(f"Your birthday, {formattedDate}, is also {holiday}!")

    except:
        print("You did not enter a valid number")

else:
    print(f"{month} is not a valid month of the year.")
