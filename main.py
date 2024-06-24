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
        print("----------- RULES -----------")
        # Prints Rules.


    # If user picks task 1. Play
    elif task.upper() == "P":
        running = False
        print("----------- PLAY -----------")
        # Keeps asking user for a difficulty until they type a valid input.
        asking: bool = True
        while asking:
            # Asks user for difficulty level they wish to proceed with.
            print(" ")
            print("Please choose your difficulty")
            print("-----------------------------")
            print("   Easy    Medium    Hard   ")
            print("-----------------------------")
            # Sets the difficulty
            difficulty = input("Type here (E, M, H): ")

            # If user picks Easy
            if difficulty.upper() == "E":
                asking = False
                print("CHOSEN DIFFICULTY: EASY")
                print("-----------------------------")
                print("QUESTION 1")
                print("What is the nearest star to planet Earth?")


            # If user picks Medium
            elif difficulty.upper() == "M":
                asking = False
                print("CHOSEN DIFFICULTY: MEDIUM")


            # If user picks Hard
            elif difficulty.upper() == "H":
                asking = False
                print("CHOSEN DIFFICULTY: HARD")


            # If input isn't valid
            else:
                print("That is an invalid option, try again.")


    # If user picks task 3. Exit
    elif task.upper() == "E":
        # Ends Program
        print("--------- GOODBYE! ---------")
        running = False
    else:
        print("That is an invalid task, try again.")
        print(" ")