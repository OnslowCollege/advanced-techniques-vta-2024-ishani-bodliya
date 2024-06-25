"""
Main.

Created by: NAME
Date: DATE
"""

# Enter your code here
# Function to recieve the chosen difficulty from user.
def ask_difficulty():
    """
    Asks user for 
    """
    asking_difficulty = True
    while asking_difficulty:
        # Asks user for difficulty level they wish to proceed with.
        print(" ")
        print("Please choose your difficulty")
        print("-----------------------------")
        print("   Easy    Medium    Hard   ")
        print("-----------------------------")
        difficulty = input("Type here (E, M, H): ")
        if difficulty.upper() == "E" or "M" or "H":
            asking_difficulty = False
            return difficulty.upper()
        else:
            print("That is an invalid option, try again.")
            print("")

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
        asking_difficulty: bool = True
        while asking_difficulty:
            # Asks user for difficulty level they wish to proceed with.
            print(" ")
            print("Please choose your difficulty")
            print("-----------------------------")
            print("   Easy    Medium    Hard   ")
            print("-----------------------------")
            # Sets the difficulty
            difficulty = input("Type here (E, M, H): ")

            # If user picks E - Easy
            if difficulty.upper() == "E":
                asking_difficulty = False
                print("CHOSEN DIFFICULTY: EASY")
                print("-----------------------------")
                print(" ")

                asking_topic_easy: bool = True
                while asking_topic_easy:
                    # Asks user for topic to get quizzed on.
                    print("Choose a topic in science: ")
                    print("-----------------------------")
                    print(" Physics  Biology  Chemistry")
                    print("-----------------------------")
                    # Sets the topic
                    topic = input("Type here (P, B, C): ")

                    # If user picks P - Physics as their topic
                    if topic.upper() == "P":
                        asking_topic_easy = False
                        print("CHOSEN TOPIC: PHYSICS")

                    # If user picks B - Biology as their topic
                    elif topic.upper() == "B":
                        asking_topic_easy = False
                        print("CHOSEN TOPIC: BIOLOGY")

                    # If user picks C - Chemistry as their topic
                    elif topic.upper() == "C":
                        asking_topic_easy = False
                        print("CHOSEN TOPIC: CHEMISTRY")
                    
                    # If input isnt valid 
                    else:
                        print("That is an invalid option, try again.")
                        print("")


            # If user picks M - Medium
            elif difficulty.upper() == "M":
                asking_difficulty = False
                print("CHOSEN DIFFICULTY: MEDIUM")
                print("-----------------------------")
                print(" ")

                asking_topic_med: bool = True
                while asking_topic_med:
                    # Asks user for topic to get quizzed on.
                    print("Choose a topic in science: ")
                    print("-----------------------------")
                    print(" Physics  Biology  Chemistry")
                    print("-----------------------------")
                    # Sets the topic
                    topic = input("Type here (P, B, C): ")

                    # If user picks P - Physics as their topic
                    if topic.upper() == "P":
                        asking_topic_med = False
                        print("CHOSEN TOPIC: PHYSICS")

                    # If user picks B - Biology as their topic
                    elif topic.upper() == "B":
                        asking_topic_med = False
                        print("CHOSEN TOPIC: BIOLOGY")

                    # If user picks C - Chemistry as their topic
                    elif topic.upper() == "C":
                        asking_topic_med = False
                        print("CHOSEN TOPIC: CHEMISTRY")
                        
                    # If input isnt valid 
                    else:
                        print("That is an invalid option, try again.")
                        print("")


            # If user picks H - Hard
            elif difficulty.upper() == "H":
                asking_difficulty_hard = False
                print("CHOSEN DIFFICULTY: HARD")
                print("-----------------------------")
                print(" ")

                asking_topic_hard: bool = True
                while asking_topic_hard:
                    # Asks user for topic to get quizzed on.
                    print("Choose a topic in science: ")
                    print("-----------------------------")
                    print(" Physics  Biology  Chemistry")
                    print("-----------------------------")
                    # Sets the topic
                    topic = input("Type here (P, B, C): ")

                    # If user picks P - Physics as their topic
                    if topic.upper() == "P":
                        asking_topic_hard = False
                        print("CHOSEN TOPIC: PHYSICS")

                    # If user picks B - Biology as their topic
                    elif topic.upper() == "B":
                        asking_topic_hard = False
                        print("CHOSEN TOPIC: BIOLOGY")

                    # If user picks C - Chemistry as their topic
                    elif topic.upper() == "C":
                        asking_topic_hard = False
                        print("CHOSEN TOPIC: CHEMISTRY")
                        
                    # If input isnt valid 
                    else:
                        print("That is an invalid option, try again.")
                        print("")

            # If input isn't valid
            else:
                print("That is an invalid option, try again.")
                print("")


    # If user picks task 3. Exit
    elif task.upper() == "E":
        # Ends Program
        print("--------- GOODBYE! ---------")
        running = False
    else:
        print("That is an invalid task, try again.")
        print(" ")