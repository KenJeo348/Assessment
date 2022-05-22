"""Component 4 (days of the week)
04_days_of_week_quiz_v4 Made cleaner
, and added better code commenting.
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

        # Asking user the first day on the shuffled list in maori
        user_answer = input(f"What is the Maori word for {days[question_number]}: ").lower()

        # If statements telling that the user is correct if they got the answer right.
        if days[question_number] == "Monday" and user_answer == "rahina":
            print("You are Correct\n")

        elif days[question_number] == "Tuesday" and user_answer == "ratu":
            print("You are Correct\n")

        elif days[question_number] == "Wednesday" and user_answer == "raapa":
            print("You are Correct\n")

        elif days[question_number] == "Thursday" and user_answer == "rapare":
            print("You are Correct\n")

        elif days[question_number] == "Friday" and user_answer == "ramere":
            print("You are Correct\n")

        elif days[question_number] == "Saturday" and user_answer == "rahoroi":
            print("You are Correct\n")

        elif days[question_number] == "Sunday" and user_answer == "ratapu":
            print("You are Correct\n")

        # Telling user they got it incorrect and canceling off the player_score += 1 with player_score -=1, (therefore 0 score)
        else:
            print("You are incorrect\n")
            player_score -= 1

        # Adding 1 to the question number and the player score for every question
        question_number += 1
        player_score += 1

    # Returning users final score after all questions
    return player_score


# Main Routine
score = 0
total_score = days_of_week_quiz(score)
print(f"Your total score was {total_score}/7")
