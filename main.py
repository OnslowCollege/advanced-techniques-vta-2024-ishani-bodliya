"""
Main.

Created by: Ishani
Date: 16/08/24
"""

# Enter your code here

# Dictoonary with questions sorted by Topic (Physics, Biology, Chemistry) - Difficulty (Easy, Medium, Hard)
questions = {
    "Physics": {
        "easy": {
            1: {
                "question": "What force keeps us on the ground?",
                "answer": "Gravity",
                "points": 10,
            },
            2: {
                "question": "What is the unit of force?",
                "answer": "Newton",
                "points": 10,
            },
            3: {
                "question": "What is the formula for calculating speed?",
                "answer": "Distance/Time",
                "points": 10,
            },
            4: {
                "question": "What is the primary cause of tides on Earth?",
                "answer": "Moon",
                "points": 10,
            },
            5: {
                "question": "What is the formula for force?",
                "answer": "mass * acceleration",
                "points": 10,
            },
        },
        "medium": {
            1: {
                "question": "What law states that for every action there is an equal and opposite reaction?",
                "answer": "Newton's third law",
                "points": 20,
            },
            2: {
                "question": "What is the formula for calculating kinetic energy?",
                "answer": "1/2 mv^2",
                "points": 20,
            },
            3: {
                "question": "What is the SI unit of power?",
                "answer": "Watt",
                "points": 20,
            },
            4: {
                "question": "An object is weightless when its...",
                "answer": "in freefall",
                "points": 20,
            },
            5: {
                "question": "Light years is the unit of...",
                "answer": "Length",
                "points": 20,
            },
        },
        "hard": {
            1: {
                "question": "What is the phenomenon where light bends around corners?",
                "answer": "Diffraction",
                "points": 30,
            },
            2: {
                "question": "What law states that for every action there is an equal and opposite reaction?",
                "answer": "Newton's third law",
                "points": 30,
            },
            3: {
                "question": "What is the theory that describes the behaviour of particles at atomic and subatomic levels?",
                "answer": "Quantum mechanics",
                "points": 30,
            },
            4: {
                "question": "What type of lens is used in a magnifying glass?",
                "answer": "Convex",
                "points": 30,
            },
            5: {
                "question": "How many minutes does it take for light to reach Earth from the Sun?",
                "answer": "8",
                "points": 30,
            },
        },
    },
    "Biology": {
        "easy": {
            1: {
                "question": "What organ pumps blood through the body?",
                "answer": "Heart",
                "points": 10,
            },
            2: {
                "question": "What is the largest organ in the human body?",
                "answer": "Skin",
                "points": 10,
            },
            3: {
                "question": "What process do plants use to make food?",
                "answer": "Photosynthesis",
                "points": 10,
            },
            4: {
                "question": "Heterochromia results in which change in physical appearance?",
                "answer": "different colored eyes",
                "points": 10,
            },
            5: {
                "question": "Botany is the study of what life-form?",
                "answer": "Plants",
                "points": 10,
            },
        },
        "medium": {
            1: {
                "question": "What is the smallest unit of life?",
                "answer:": "Cell",
                "points": 20,
            },
            2: {
                "question": "What is the powerhouse of the cell?",
                "answer": "Mitochondria",
                "points": 20,
            },
            3: {
                "question": "What is the longest bone in the human body?",
                "answer": "Femur",
                "points": 20,
            },
            4: {
                "question": "What shape are plant cells",
                "answer": "Rectangular",
                "points": 20,
            },
            5: {
                "question": "What molecule carries genetic instructions used in growth, development, and reproduction",
                "answer": "DNA",
                "points": 20,
            },
        },
        "hard": {
            1: {
                "question": "What is the scientific name for the human species?",
                "answer": "Homo sapiens",
                "points": 30,
            },
            2: {
                "question": "What part of the cell contains the genetic material?",
                "answer": "Nucleus",
                "points": 30,
            },
            3: {
                "question": "What is the proces by which a single cell divides into two identical cells?",
                "answer": "Mitosis",
                "points": 30,
            },
            4: {
                "question": "What is the study of heredity and the variation of inherited characteristics?",
                "answer": "Genetics",
                "points": 30,
            },
            5: {
                "question": "What organ is the main component of plant cell walls?",
                "answer": "Cellulose",
                "points": 30,
            },
        },
    },
    "Chemistry": {
        "easy": {
            1: {
                "question": "What is H2O commonly known as?",
                "answer": "Water",
                "points": 10,
            },
            2: {
                "question": "What is the first element on the periodic table?",
                "answer": "Hydrogen",
                "points": 10,
            },
            3: {
                "question": "What as do plants absorb from the atmosphere?",
                "answer": "Carbon",
                "points": 10,
            },
            4: {
                "question": "What is the heaviest naturally occurring element?",
                "answer": "Uranium",
                "points": 10,
            },
            5: {
                "question": "What type of charge does an electron carry?",
                "answer": "Positive",
                "points": 10,
            },
        },
        "medium": {
            1: {
                "question": "What is the pH of pure water",
                "answer": "7",
                "points": 20,
            },
            2: {
                "question": "What is the chemical symbol for gold?",
                "answer": "Au",
                "points": 20,
            },
            3: {
                "question": "What type of bond involves the sharing of electron pairs between atoms?",
                "answer": "Covalent bond",
                "points": 20,
            },
            4: {
                "question": "What is the process called when a solid turns directly into a gas?",
                "answer": "Sublimation",
                "points": 20,
            },
            5: {
                "question": "True or False, Acids have a pH of below 7",
                "answer": "True",
                "points": 20,
            },
        },
        "hard": {
            1: {
                "question": "What is the chemical formula for table salt?",
                "answer": "NaCl",
                "points": 30,
            },
            2: {
                "question": "What is the heaviest naturally occuring element?",
                "answer": "Uranium",
                "points": 30,
            },
            3: {
                "question": "What is the main component of natural gas?",
                "answer": "Methane",
                "points": 30,
            },
            4: {
                "question": "K is the chem symbol of which element?",
                "answer": "Potaaaium",
                "points": 30,
            },
            5: {
                "question": "At room temperature, what is the only metal that is in liquid form?",
                "answer": "Mercury",
                "points": 30,
            },
        },
    },
}


# Functions
def ask_difficulty():
    """
    Asks the user to select a difficulty level for the quiz.

    Returns:
    -------
    str or None
    - The chosen difficulty as an uppercase letter ('E' for Easy, 'M' for Medium, 'H' for Hard)
    - If valid option is selected. Returns None if no valid option is selected.

    """
    asking_difficulty = True
    while asking_difficulty:
        # Asks user for difficulty level they wish to proceed with.
        print(" ")
        print("Please choose your difficulty")
        print("-----------------------------")
        print("   Easy    Medium    Hard   ")
        print("-----------------------------")
        # Sets the topic
        difficulty = input("Type here (E, M, H): ").upper()
        # Checks if the difficulty which is inputted is valid or not
        if difficulty in ["E", "M", "H"]:
            asking_difficulty = False
            # Checks which valid input was typed in and returns the set of questions to the user
            match difficulty:
                case "E":
                    return "easy"
                case "M":
                    return "medium"
                case "H":
                    return "hard"
        print("That is an invalid option, try again.")
        print("")
    return None


def ask_topic():
    """
    Ask user to select a topic based on the chosen difficulty level.

    Args:
    ----
    difficulty : str
        The difficulty level chosen by the use.

    Returns:
    -------
    str or None
    - The chosen topic as an uppercase letter ('P' - Physics, 'B' - Biology, 'C' - Chemistry)
    - If valid option is selected. Returns None if no valid option is selected.

    """
    asking_topic = True
    while asking_topic:
        # Asks user for topic to get quizzed on.
        print("Choose a topic in science: ")
        print("-----------------------------")
        # Prints valid options for users.
        print(" Physics  Biology  Chemistry")
        print("-----------------------------")
        # Sets the topic
        topic = input("Type here (P, B, C): ").upper()
        # Checks if the difficulty which is inputted is valid or not
        if topic in ["P", "B", "C"]:
            asking_topic = False
            match topic:
                case "P":
                    return "Physics"
                case "B":
                    return "Biology"
                case "C":
                    return "Chemistry"
        print("That is an invalid option, try again.")
        print("")
    return None


def play_game():
    """Start asking question when user picks play button."""
    print("----------- PLAY -----------")
    # Asks and prints the set difficulty
    difficulty = ask_difficulty()
    print(f"CHOSEN DIFFICULTY: {difficulty}")
    print("-----------------------------")
    print(" ")

    # Asks and prints the set topic
    topic = ask_topic()
    print("-----------------------------")
    print(f"CHOSEN TOPIC: {topic}")

    total_points = 0
    do_gamble = False

    # Get the total number of questions based on the chosen topic and difficulty
    num_questions = len(questions[topic][difficulty])

    # Prints the questions based off the set topic and difficulty
    for question_num in range(1, num_questions + 1):
        print(f"Question {question_num}")
        print(f"Current points: {total_points}")
        # Ask the current question and store the points awarded
        points = ask_questions(topic, difficulty, question_num)
        # If the user answered correctly and has chosen to gamble
        if points > 0 and do_gamble:
            points = points * 2
            print(f"Correct! + {points} points")
            total_points += points

            # If it isn't the last question, ask if they want to gamble on the next question
            if question_num != num_questions:
                print("-----------------------------")
                print(
                    """Do you want to bet your points on answering the next question correct?
Answering correctly will give double points while answering incorrect will loose you as many points as you would have gained."""
                )
                print("-----------------------------")

                # Check if the user wants to gamble on the next question
                if input("Type Y for to bet, anything else to not: ").upper() == "Y":
                    do_gamble = True
                else:
                    do_gamble = False

        # If the user answered incorrectly and had gambled, deduct points
        elif points > 0:
            print(f"Correct! + {points} points")
            total_points += points
            if question_num != num_questions:
                print("")
                print("-----------------------------")
                print(
                    """Do you want to bet your points on answering the next question correct?
Answering correctly will give double points while answering incorrect will loose you as many points as you would have gained."""
                )
                print("-----------------------------")

                # Asks user for their answer
                while True:
                    user_input = input("Type Y to bet, N to not: ").upper()
                    if user_input in ["Y", "N"]:
                        print("-----------------------------")
                        print("")
                        do_gamble = (user_input == "Y")
                        break
                    print("Invalid input. Please type 'Y' to bet or 'N' to not.")

        # If the user answered incorrectly and had gambled, deduct points
        elif points == 0 and do_gamble:
            points = questions[topic][difficulty][question_num]["points"]
            print(f"You lose {points} points")
            print("-----------------------------")
            total_points -= points

            # Reset gambling option to False after a loss
            do_gamble = False
    # End of the game: Display the total points
    print(f"Game over. Total points: {total_points}")


def ask_questions(topic, difficulty, question_num):
    """
    Ask a question based on topic and difficulty, and returns the points.

    Arguments:
    ---------
    topic : str
    - The category or subject of the question.
    difficulty : str
    - The difficulty level of the question.
    question_num : int
    - The number of the question within the topic and difficulty level.

    Returns:
    -------
    int: The points for correct answer. If incorrect, returns 0.

    """
    try:
        # Gets the question info using the topic, difficulty, and question number.
        question_info = questions[topic][difficulty][question_num]
    except KeyError as e:
        # If the question number doesn't exist, prints error message and return 0 points.
        print(f"Error: Question number {question_num} not found - {e}")
        return 0

    # Display the question to the user.
    print(question_info["question"])
    print("-----------------------------")
    user_answer = input("Your answer: ").strip()
    answer = question_info["answer"].lower()
    # Compares user's answer with the correct answer, ignoring case and spaces.
    if user_answer.lower().replace(" ", "") == answer.replace(" ", ""):
        return question_info["points"]

    # If answer is incorrect, shows the correct answer and returns 0 points.
    print(f"Incorrect. The correct answer is: {question_info['answer']}")
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
