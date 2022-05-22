"""Component 4 (days of the week)
Recovered all the days of the week, and made it into a full quiz
Temporarily got rid of random list shuffler for testing convenience
Based on 04_days_of_week_quiz_v2
"""


# Variables and lists
player_score = 0
question_number = 0
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# While loop repeating until the user has gone through all the days.
while question_number < 7:

    # Asking user the question everytime the while loop 'loops'.
    user_answer = input(f"What is the Maori word for {days[question_number]}: ").lower()

    # Testing if the answer was right for every day.
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

    # If the user wasn't right printing 'You are incorrect'.
    # Taking one off player_score to cancel off player_score += 1 from later on.
    else:
        print("You are incorrect")
        player_score -= 1

    # Adding 1 to the question_number and player score everytime the while loop 'loops'.
    question_number += 1
    player_score += 1


# Main Routine
print(f"Your total score was {player_score}/7")

