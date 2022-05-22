"""Component 5 (Numbers 1-10 quiz)
05_numbers_quiz_v1 made into a quiz,
without shuffling the list for testing convenience
"""

import random

question_number = 0
# List of the days
days = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
        [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]]

# While loop that repeats for all numbers
while question_number < 10:

    # Asking the user the question.
    user_answer = input(f"What is the number {days[question_number][0]} in Maori: ").lower()

    # Checking Users answer.
    if user_answer == days[question_number][1]:
        print("You are correct")
    else:
        print("You are incorrect")
    question_number += 1
