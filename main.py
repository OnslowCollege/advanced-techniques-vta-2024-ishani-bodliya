"""
Main.

Created by: NAME
Date: DATE
"""

# Enter your code here
questions = {
    "Physics": {
        "easy": {
            1: {"question": "What force keeps us on the ground?", "answer": "Gravity", "points": 10}
        },
        "medium": {
            1: {"question": "What law states that for every action there is an equal and opposite reaction?", "answer:": "Newton's third law", "points": 20}
        },
        "hard": {
            1: {"question": }
        }
    }
}

# Functions
def ask_difficulty():
    """
    Ask user for  their chosen difficuly to pursue the program and will determine contents of the questions.

    Returns:
    -------
    - A difficulty that is converted to uppercases.

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
        if difficulty.upper() in ["E", "M", "H"]:
            asking_difficulty = False
            return difficulty.upper()
        print("That is an invalid option, try again.")
        print("")
    return None


def ask_topic(difficulty):
    """
    Ask user which topic they would like to be quizzed on.

    Arguments:
    ---------
    - difficulty: The difficulty of questions set by the user.

    Return:
    ------
    - A topic that is converted to uppercases.

    """
    asking_topic = True
    while asking_topic:
    # Asks user for topic to get quizzed on.
        print("Choose a topic in science: ")
        print("-----------------------------")
        print(" Physics  Biology  Chemistry")
        print("-----------------------------")
        # Sets the topic
        topic = input("Type here (P, B, C): ")
        if topic.upper() in ["P", "B", "C"]:
            asking_topic = False
            return topic.uper()
        print("That is an invalid option, try again.")
        print("")
    return None


def play_game():
    """Start asking question when user picks play button."""
    print("----------- PLAY -----------")
    difficulty = ask_difficulty()
    print(f"CHOSEN DIFFICULTY: {difficulty}")
    print("-----------------------------")
    print(" ")

    topic = ask_topic(difficulty)
    print(f"CHOSEN TOPIC: {topic}")


# Main code loop
running = True
while running:
    # Introduces program.
    print("Welcome to the Science Quiz!")
    print("---------------------------")
    # Prints valid tasks for users.
    print("  Exit    Play    Rules  ")
    print("---------------------------")
    # Asks user which function they would like to perform.
    task = input("Choose an action (E, P, R): ")
    print("")

    # If user picks task 2. Rules
    if task.upper() == "R":
        print("----------- RULES -----------")
        print("• Choose Difficulty (Easy, Medium, Hard)")
        print("• Select topic of choice (Physics, Biology, Chemistry)")
        print("• Answer every question to your bestest ability")
        print("• Enjoy learning!")
        print("-----------------------------")
        input("Press enter when your finished reading :)")
        print("")
        # Prints Rules. (choose diff, select topic, answer ques,enjoy learn)

    # If user picks task 1. Play
    elif task.upper() == "P":
        play_game()
        running = False
    # If user picks task 3. Exit
    elif task.upper() == "E":
        # Ends Program
        print("--------- GOODBYE! ---------")
        running = False
    else:
        print("That is an invalid task, try again.")
        print(" ")