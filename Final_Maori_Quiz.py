"""This is the final version of my Maori Quiz,
it is assembled with all the updated versions of the components.
This quiz tests the user on their maori knowledge and shows their score."""


# 'import random' for random question generator
import random


# Function asking if user has played before.
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
            print()
            print("Please enter either Y/N or Yes/No\n")


# Function that displays instructions
def instructions():
    # Instruction texts
    print()
    print("<== How to Play == >\n"
          "\n"
          "You would get to choose between two quiz's\n"
          "'Days of The week in Maori' or 'Numbers 1 - 10 in Maori\n"
          "After you choose you will get redirected to your chosen quiz\n"
          "You would have to write the displayed Day/Number in Maori/Te Reo'\n"
          "\n"
          "After answering each question you will get told if you were right or wrong.\n"
          "Your final score would be displayed at the end of the quiz, and you can either try again or leave the program.\n"
          "\n"
          "Do you think you can get all the questions right?")
    print("-" * 50)
    print()


# Function that gives the user a choice of which quiz to do, or (quit)
def quiz_chooser():
    score = 0
    valid = False
    # Keep asking until a valid number has been inputted 0 - 2
    while not valid:
        try:
            # Options to choose from
            print("0: Quit the Program\n"
                  "1: Redirects to Days of the Week quiz\n"
                  "2: Redirects to Numbers 1-10 quiz\n")
            # Asking for choice
            choose_quiz = int(input("Choose one of the options above and press enter: "))
            print()

            # If the user inputs 0, output 'Goodbye' than quit the program
            if choose_quiz == 0:
                print(formatter("~", "Goodbye"))
                exit()

            # If the user inputs 1, redirect to the days of the week quiz.
            elif choose_quiz == 1:
                total_score = days_of_week_quiz(score)
                print(f"Your total score was {total_score}/7")
                print()
                valid = True

            # If the user inputs 2, redirect to the numbers quiz.
            elif choose_quiz == 2:
                total_score = numbers_quiz(score)
                print(f"Your total score was {total_score}/10")
                print()
                valid = True

        # If the user enters an invalid answer, output 'Please enter a valid answer'
            else:
                print()
                print(formatter("#", "Please enter a valid answer."))
                print()

        except ValueError:
            print()
            print(formatter("#", "Please enter a valid answer."))
            print()


# Function containing days of the week quiz
def days_of_week_quiz(_quiz_score):
    # Variables and lists
    player_score = 0
    question_number = 0
    days = [["Monday", "Rahina"], ["Tuesday", "Ratu"], ["Wednesday", "Raapa"], ["Thursday", "Rapare"],
            ["Friday", "Ramere"], ["Saturday", "Rahoroi"], ["Sunday", "Ratapu"]]
    # Shuffling the (days) list in a random order for the quiz.
    random.shuffle(days)

    # Welcome message
    print(formatter("-", "Welcome to the Days of the week quiz"))
    print()

    # While loop, repeating until the user has gone through all the days.
    while question_number < 7:

        # Asking user the day in order of the shuffled list.
        user_answer = input(f"What is the Maori word for {days[question_number][0]}: ").title()
        print()

        # If the user got it right, output, "You are correct"
        if user_answer == days[question_number][1]:
            player_score += 1
            print(formatter("=", "You are correct"))
            print()
        # If the user got it wrong, output, "You are incorrect"
        else:
            print(formatter("*", "You are incorrect"))
            print()

        # Adding 1 to the question number after every question
        question_number += 1

    # Returning users final score after all questions
    return player_score


# Function containing numbers quiz
def numbers_quiz(_quiz_score):
    # Variables
    player_score = 0
    question_number = 0
    # List of the days
    numbers = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
               [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]]
    # Shuffling the numbers list in a random order
    random.shuffle(numbers)

    # Welcome message
    print(formatter("-", "Welcome to the Numbers quiz"))
    print()

    # While loop that repeats the quiz until the user has gone through all numbers 1 - 10.
    while question_number < 10:

        # Asking user the number in order of the shuffled list.
        user_answer = input(f"What is the number {numbers[question_number][0]} in Maori: ").lower()
        print()

        # If the user got it right, output 'You are correct'
        if user_answer == numbers[question_number][1]:
            player_score += 1
            print(formatter("=", "You are correct"))
            print()
        # If the user got it wrong, output 'You are correct'
        else:
            print(formatter("*", "You are incorrect"))
            print()

        # Adding 1 to the question number after every question
        question_number += 1

    # Returning the players score
    return player_score


# Formatter Function
def formatter(symbol, text):

    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom} \n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("-", "Welcome to the Maori quiz"))
print()

# Asking the user if they have played before (yes/no function)
tried_before = yes_no("Have you tried the quiz before? (Y for yes/N for No): ")
print()

# If the user said no redirecting to the instructions.
if tried_before == "no":
    instructions()

play_again = ""

# While loop that repeats the quiz chooser function and the quizzes until user wants to exit.
while play_again != "x":
    if play_again == "":
        quiz_chooser()
    else:
        print("Please enter a valid answer\n")
    play_again = input("Do you want to play again (<enter> to play, or 'x' to quit): ")
    print()
print(formatter("~", "Goodbye"))
