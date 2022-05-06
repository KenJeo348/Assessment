"""Component 4 (days of the week)
04_days_of_week_quiz_v3 made into a function
"""

import random


def days_of_week_quiz(_quiz_score):
    # Variables and lists
    player_score = 0
    question_number = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Shuffling the (days) list in a random order for the quiz.
    random.shuffle(days)

    # While loop repeating until the user has gone through all the days.
    while question_number < 7:

        user_answer = input(f"What is the Maori word for {days[question_number]}: ").lower()

        if days[question_number] == "Monday" and user_answer == "rahina":
            print("You are Correct")

        elif days[question_number] == "Tuesday" and user_answer == "ratu":
            print("You are Correct")

        elif days[question_number] == "Wednesday" and user_answer == "raapa":
            print("You are Correct")

        elif days[question_number] == "Thursday" and user_answer == "rapare":
            print("You are Correct")

        elif days[question_number] == "Friday" and user_answer == "ramere":
            print("You are Correct")

        elif days[question_number] == "Saturday" and user_answer == "rahoroi":
            print("You are Correct")

        elif days[question_number] == "Sunday" and user_answer == "ratapu":
            print("You are Correct")

        else:
            print("You are incorrect")
            player_score -= 1

        question_number += 1
        player_score += 1
    return player_score


# Main Routine
score = 0
total_score = days_of_week_quiz(score)
print(f"Your total score was {total_score}/7")
