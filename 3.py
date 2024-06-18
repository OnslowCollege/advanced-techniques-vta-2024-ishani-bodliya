"""
Main.

Created by: NAME
Date: DATE
"""

# Enter your code here
# Introduces program.
print("Welcome to the Science Quiz!")
print("------------------------------")
# Prints valid tasks for users.
print("1. Play")
print("2. Rules")
print("3. Exit")
print("------------------------------")
# Asks user which function they would like to perform.
task = int(input("Choose an action: "))

# If user picks task 2. Rules
if task == 2:
    print("--- RULES ---")
    # Prints Rules.

# If user picks task 1. Play
elif task == 1:
    print("--- PLAY ---")
    # Asks user for difficulty level they wish to proceed with.

# If user picks task 3. Exit
elif task == 3:
    # Ends Program
    print("--- GOODBYE! ---")