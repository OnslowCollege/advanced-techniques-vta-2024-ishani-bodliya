"""
Main.

Created by: NAME
Date: DATE
"""

# Enter your code here
questions = {
    "Physics": {
        "easy": {
            1: {"question": "What force keeps us on the ground?", "answer": "Gravity", "points": 10},
            2: {"question": "What is the unit of force?", "answer": "Newton", "points": 10},
            3: {"question": "Wha is the formula for calculating speed?", "answer": "Distance/Time", "points": 10},
            4: {"question": "What is the primary cause of tides on Earth?", "answer": "Moon", "points": 10},
            5: {"question": "What is the formula for force?", "answer": "mass * acceleration", "points": 10}
        },
        "medium": {
            1: {"question": "What law states that for every action there is an equal and opposite reaction?", "answer:": "Newton's third law", "points": 20},
            2: {"question": "What is the formula for calculating kinetic energy?", "answer": "1/2 mv^2", "points": 20},
            3: {"question": "What is the SI unit of power?", "answer": "Watt", "points": 20},
            4: {"question": "", "answer": "", "points": 20},
            5: {"question": "", "answer": "", "points": 20},
        },
        "hard": {
            1: {"question": "What is the phenomenon where light bends around corners?", "answer": "Diffraction", "points": 30 },
            2: {"question": "What law states that for every action there is an equal and opposite reaction?", "answer": "Newton's third law", "points": 30 },
            3: {"question": "What is the theory that describes the behaviour of particles at atomic and subatomic levels?", "answer": "Quantum mechanics", "points": 30 },
            4: {"question": "", "answer": "", "points": 30},
            5: {"question": "", "answer": "", "points": 30}
        }
    },


    "Biology": {
        "easy": {
            1: {"question": "What organ pumps blood through the body?", "answer": "Heart", "points": 10},
            2: {"question": "", "answer": "", "points": 10},
            3: {"question": "", "answer": "", "points": 10},
            4: {"question": "", "answer": "", "points": 10},
            5: {"question": "", "answer": "", "points": 10}
        },
        "medium": {
            1: {"question": "What process do plants use to make food?", "answer:": "Photosynthesis", "points": 20},
            2: {"question": "What is the powerhouse of the cell?", "answer": "Mitochondria", "points": 20},
            3: {"question": "What is the longest bone in the human body?", "answer": "Femur", "points": 20},
            4: {"question": "", "answer": "", "points": 10},
            5: {"question": "", "answer": "", "points": 10}
            
        },
        "hard": {
            1: {"question": "What is the scientific name for the human species?", "answer": "Homo sapiens", "points": 30 },
            2: {"question": "What part of the cell contains the genetic material?", "answer": "Nucleus", "points": 30},
            3: {"question": "", "answer": "", "points": 10},
            4: {"question": "", "answer": "", "points": 10},
            5: {"question": "", "answer": "", "points": 10}
        }
    },


    "Chemistry": {
        "easy": {
            1: {"question": "What is H2O commonly known as?", "answer": "Water", "points": 10},
            2: {"question": "What is the first element on the periodic table?", "answer": "Hydrogen", "points": 10},
            3: {"question": "", "answer": "", "points": 10},
            4: {"question": "", "answer": "", "points": 10},
            5: {"question": "", "answer": "", "points": 10}
        },
        "medium": {
            1: {"question": "What is the pH of pure water", "answer:": "7", "points": 20},
            2: {"question": "What is the chemical symbol for gold?", "answer": "Au", "points": 20},
            3: {"question": "", "answer": "", "points": 10},
            4: {"question": "", "answer": "", "points": 10},
            5: {"question": "", "answer": "", "points": 10}
        },
        "hard": {
            1: {"question": "What is the chemical formula for table salt?", "answer": "NaCl", "points": 30 },
            2: {"question": "What is the heaviest naturally occuring element?", "answer": "Uranium", "points": 30 },
            3: {"question": "", "answer": "", "points": 10},
            4: {"question": "", "answer": "", "points": 10},
            5: {"question": "", "answer": "", "points": 10}
            
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
    Ask user which topic they would like to be quizzed on from Physics, Biology, or Chemistry.

    Arguments:
    ---------
    - difficulty: The difficulty of questions set by the user.
    - asking_topic: States wether program is waiting for a valid answer or not.

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
            return topic.upper()
        print("That is an invalid option, try again.")
        print("")
    return None


def uncertain_reward(points):
    """
    Determine the uncertain reward that user recieve when they answer correctly.

    Arguments:
    ---------
    - points: The number of points the user earned.

    Returns:
    -------
    - The updated points if the user wins the uncertain reward.
    - If user loses the uncertain reward, return is 0.

    """
    chance_for_reward = random.choice([True, False])
    if chance_for_reward:
        return points * 2
    return 0


def play_game():
    """Start asking question when user picks play button."""
    print("----------- PLAY -----------")
    difficulty = ask_difficulty()
    print(f"CHOSEN DIFFICULTY: {difficulty}")
    print("-----------------------------")
    print(" ")

    topic = ask_topic(difficulty)
    print(f"CHOSEN TOPIC: {topic}")

    total_points = 0

    num_questions = len(questions[topic.lower()][difficulty.lower()])
    for question_num in range (1, num_questions + 1):
        print(f"Question {question_num}")
        points = ask_questions(topic.lower(), difficulty.lower(), question_num)

        if points > 0:
            print(f"Correct! + {points} points")
            total_points += points
            points_from_reward = uncertain_reward(points)
            if points_from_reward > 0:
                print("You won the uncertain reward, your points were doubled")
                total_points += points_from_reward
                print(f"Points: {points}")
            else:
                print("You lost the uncertain reward and lost points")
                total_points -= points
                print(f"Points: {points}")
        else:
            print("Incorrect answer.")
    print(f"Game over. Points: {points}")


def ask_questions(topic, difficulty, question_num):
    question = questions[topic][difficulty][question_num]["question"]
    answer = questions[topic][difficulty][question_num]["answer"]
    points = questions[topic][difficulty][question_num]["points"]
    users_answer = input(question + " ")

    if users_answer.lower() == answer.lower():
        return points
    return 0


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