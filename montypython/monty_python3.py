#!/usr/bin/env python3

round = 0
answer = ""

while round < 3 and answer != "brian" and answer != "shrubbery":
    round += 1

    print('Finish the movie title, "Monty Python\'s The Life of ______"')

    answer = input("Your guess -->").lower()
    
    if answer == "brian":
        print("Correct!")
    elif answer == "shrubbery":
        print("Ni!")
    elif round == 3:
        print('Sorry, the correct answer was "Brian".')
    else:
        print('Sorry. Try Again!')
