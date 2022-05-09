"""Component 4 (Days of the week quiz)
Generate the numbers from 1-10 in a random order
"""

import random


def numbers_quiz(_quiz_score):
    player_score = 0
    question_number = 0
    # List of the days
    numbers = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
            [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]]
    random.shuffle(numbers)

    while question_number < 10:

        user_answer = input(f"What is the number {numbers[question_number][0]} in Maori: ").lower()

        if user_answer == numbers[question_number][1]:
            player_score += 1
            print("you are correct")
        else:
            print("You are incorrect")

        question_number += 1
    return player_score


# Main routine
