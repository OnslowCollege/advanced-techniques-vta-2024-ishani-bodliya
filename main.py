"""
Main.

Created by: NAME
Date: DATE
"""

# Enter your code here
# Allows program to repeat itself until user types a valid answer.
running: bool = True
while running:
    # Introduces program.
    print("Welcome to the Science Quiz!")
    print("---------------------------")
    # Prints valid tasks for users.
    print("  Exit    Play    Rules  ")
    print("---------------------------")
    # Asks user which function they would like to perform.
    task = input("Choose an action (E, P, R): ")

    # If user picks task 2. Rules
    if task.upper() == "R":
        running = False
        print("--- RULES ---")
        # Prints Rules.

    # If user picks task 1. Play
    elif task.upper() == "P":
        running = False
        print("--- PLAY ---")
        # Asks user for difficulty level they wish to proceed with.
        while running

    # If user picks task 3. Exit
    elif task.upper() == "E":
        # Ends Program
        print("--- GOODBYE! ---")
        running = False
    else:
        print("That is an invalid task, try again.")
        print(" ")