#!/usr/bin/env python3

grade = ""

score = float(input("Please enter your score: "))

if score >= 90:
    grade = "A! Superb!"
elif score >= 80:
    grade = "B! Great Job!"
elif score >= 70:
    grade = "C! Not Bad!"
elif score >= 60:
    grade = "D! You did it!"
else:
    grade = "F! Try harder!"

print(f"Your Grade is: {grade}")
