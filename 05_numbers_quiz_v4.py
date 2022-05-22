"""Component 5 (Numbers 1-10 quiz)
05_numbers_quiz_v3 made into a function
"""

import random


def numbers_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_number = 0

    # List of the days
    numbers = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
            [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]]

    # Shuffling the list in a random order
    random.shuffle(numbers)

    # Looping test for all numbers between 1-10.
    while question_number < 10:

        # Asking user the question.
        user_answer = input(f"What is the number {numbers[question_number][0]} in Maori: ").lower()

        # Checking if the user got the question right, or wrong.
        if user_answer == numbers[question_number][1]:
            player_score += 1
            print("you are correct")
        else:
            print("You are incorrect")

        # Increasing the question number by 1 every time the while loop 'loops'.
        question_number += 1
    return player_score


# Main routine
score = 0
total_score = numbers_quiz(score)
print(f"Your total score was {total_score}/10")
