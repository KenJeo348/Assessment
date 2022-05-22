"""Component 4 (days of the week)
Got rid of all the days except for Monday for testing convenience
Based on 04_days_of_week_quiz_v1
"""

import random

question_number = 0
# List with only 'Monday' left
days = ["Monday"]
# Has no affect now, but will do later.
random.shuffle(days)

# While loop for testing convenience will finish after 7 goes.
while question_number < 7:
    # Asking user the question.
    user_answer = input(f"What is the Maori word for {days[0]}").lower()

    # If their answer was right, print 'You are correct'
    if user_answer == "rahina":
        print("You are correct\n")

    # Else print, 'You are incorrect'
    else:
        print("You are incorrect\n")

    question_number += 1
