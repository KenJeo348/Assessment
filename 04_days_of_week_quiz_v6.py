"""Component 4 (days of the week)
04_days_of_week_quiz_v4 Made cleaner
, and added more code commenting.
"""

import random


def days_of_week_quiz(_quiz_score):
    # Variables and lists
    player_score = 0
    question_number = 0
    days = [["Monday", "Rahina"], ["Tuesday", "Ratu"], ["Wednesday", "Raapa"], ["Thursday", "Rapare"],
            ["Friday", "Ramere"], ["Saturday", "Rahoroi"] , ["Sunday", "Ratapu"]]
    # Shuffling the (days) list in a random order for the quiz.
    random.shuffle(days)

    # While loop repeating until the user has gone through all the days.
    while question_number < 7:

        # Asking user the first day on the shuffled list in maori
        user_answer = input(f"What is the Maori word for {days[question_number][0]}: ").title()

        if user_answer == days[question_number][1]:
            player_score += 1
            print("you are correct")
        else:
            print("You are incorrect")

        # Adding 1 to the question number and the player score for every question
        question_number += 1

    # Returning users final score after all questions
    return player_score


# Main Routine
score = 0
total_score = days_of_week_quiz(score)
print(f"Your total score was {total_score}/7")
