#!/usr/bin/env python3

#Define constants and variables
VALID_OPERATORS = ["+","-","*","/"]

num1 = 0.0
num2 = 0.0
operator = ""
isInputValid = False

#Calculation functions
def add(a, b): return(a + b)
def subtract(a, b): return(a - b)
def multiply(a, b): return(a * b)
def divide(a, b): return(a / b)

#Get and test user input
while not isInputValid:

    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except:
        print("That is not a number. Please enter a number.")
        continue

    operatorHelpText = f"[{' '.join(VALID_OPERATORS)}]"
    operator = input(f"Operation? {operatorHelpText}: ")

    if operator not in VALID_OPERATORS:
        print(f"That is not a valid operation. Select one of the following: {operatorHelpText}")
        continue

    isInputValid = True

#Calculate
if operator == "+":
    print(add(num1, num2))
elif operator == "-":
    print(subtract(num1, num2))
elif operator == "*":
    print(multiply(num1, num2))
elif operator == "/" and num2 != 0:
    print(divide(num1, num2))
else:
    print("Silly goose! You can't divide by zero!") #Protecting the universe from implosion.
