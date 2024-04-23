#

import random


user_input = "yes" 

while user_input == "yes":
    user_input = input("Do you want to roll the die!! (yes \ no): ")
    if user_input == "yes":
        # roll a die --> 1 - 6
        num_die = random.randint(1, 6)
        # print the value we got after rolling 
        print("You got the number: ", num_die)
        # repeat --> until user say no
    else:
        user_input = "No"
        print("Exit... ")
           