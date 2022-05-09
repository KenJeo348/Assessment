"""Component 4 (Days of the week quiz)
Generate the numbers from 1-10 in a random order
"""

import random

player_score = 0
question_number = 0
# List of the days
days = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
        [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]]
random.shuffle(days)

while question_number < 10:

    user_answer = input(f"What is the number {days[question_number][0]} in Maori: ").lower()

    if user_answer == days[question_number][1]:
        player_score += 1
        print("you are correct")
    else:
        print("You are incorrect")

    question_number += 1

print(f"Your score was {player_score}/10.")
