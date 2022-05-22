"""Component 5 (Numbers 1-10 quiz)
Added list shuffler and main routine
Based on 05_numbers_quiz_v2
"""

import random

# Variables
player_score = 0
question_number = 0

# List of the days
days = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
        [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]]

# Shuffling list in a random order.
random.shuffle(days)

# While loop that repeats for all numbers between 1-10
while question_number < 10:

    # Asking user the question
    user_answer = input(f"What is the number {days[question_number][0]} in Maori: ").lower()

    # Checking if the user got the answer right, or wrong.
    if user_answer == days[question_number][1]:
        player_score += 1
        print("You are correct")
    else:
        print("You are incorrect")

    question_number += 1


# Main routine
print(f"Your score was {player_score}/10.")
