
import random


def yes_no(question_text):
    while True:

        # Ask the user if the have played before
        answer = input(question_text).lower()

        # If they say yes, return Yes
        if answer == "y" or answer == "yes":
            answer = "yes"
            return answer

        # If they say no, return No
        elif answer == "n" or answer == "no":
            answer = "no"
            return answer

        # Otherwise - show error
        else:
            print("Please enter either Y/N or Yes/No")


def instructions():
    print()
    print("<== How to Play == >\n"
          "\n"
          "A random day of the week would be displayed to you.\n"
          "You would have to write the displayed day in Maori/Te Reo\n"
          "\n"
          "After answering each question you will get told if you were right or wrong.\n"
          "Your final score would be displayed at the end of the quiz, and you can either try again or leave the program.\n"
          "\n"
          "Do you think you can get all the questions right?")
    print("-" * 50)
    print()


def continue_or_quit_function():
    continue_or_quit = "Starting string"
    while continue_or_quit != "":
        # Ask the user if they want to continue to the quiz.
        continue_or_quit = input("Do you want to continue to the quiz? <enter> to continue or 'x' to quit:").lower()

        # If the user inputs <enter>, output 'Program continues to quiz.
        if continue_or_quit == "":
            print()

        # If the user inputs 'x', output 'You have quit the program', and a farewell message.
        elif continue_or_quit == "x":

            print("You have quit the program.\n"
                  "We hope we could see you again.")
            exit()
        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Please enter a valid answer. <enter> to play, or 'x' to quit.")


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


# Main routine
tried_before = yes_no("Have you tried the quiz before? (Y for yes/N for No): ")

if tried_before == "no":
    instructions()

continue_or_quit_function()

score = 0
total_score = days_of_week_quiz(score)
print(f"Your total score was {total_score}/7")
