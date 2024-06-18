"""
Main.

Created by: NAME
Date: DATE
"""

valid_tasks: ["E", "P", "R", "Exit", "Play", "Rules"]

# Enter your code here
# Introduces Program
print("Welcome to the Science Quiz!")
print("------------------------------")
# Prints Tasks for user to pick from
print("   Exit     Play     Rules   ")
print("------------------------------")

# Asks user which task they would like to choose
task = input("Choose an action: ")

# Checks if answer is valid
if task in valid_tasks:
    # If user chose to see the Rules
    if task.upper() == "R" or "Rules":
        # Print rules
        print("--- RULES ---")
    elif task.upper() == "P" or "Play":
        # Asks which difficulty the player wishes to pick
        print("--- PLAY ---")
    else:
        # Ends program
        pass
else:
    print(" That is an invalid answer, Try agian")