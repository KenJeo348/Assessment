"""Component 4 (days of the week)
Got rid of all the days except for Monday for testing convenience
Based on 04_days_of_week_quiz_v1
"""

import random

question_number = 0
days = ["Monday"]
random.shuffle(days)

# While loop for testing convenience
while question_number < 7:
    days = ["Monday"]

    user_answer = input(f"What is the Maori word for {days[0]}").lower()
    if user_answer == "rahina":
        print("you are correct\n")
    else:
        print("You are incorrect\n")
