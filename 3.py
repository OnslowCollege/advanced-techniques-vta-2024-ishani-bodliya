"""
Main.

Created by: NAME
Date: DATE
"""

# Enter your code here
# Introduces program.
# Allows program to repeat itself until user types a valid answer.
running: bool = True
while running:
    print("Welcome to the Science Quiz!")
    print("---------------------------")
    # Prints valid tasks for users.
    print("  Exit    Play    Rules  ")
    print("---------------------------")
    # Asks user which function they would like to perform.
    task = int(input("Choose an action (E, P, R): "))

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
        running = False