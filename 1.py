"""
Main.

Created by: NAME
Date: DATE
"""

# Enter your code here
# Introduces program and displays all valid tasks.
print("""
    Welcome to the Science Quiz!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1. Play
    2. Rules
    3. Exit
    ------------------------------
    """)

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