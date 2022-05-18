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
          "You would get to choose between two quiz's\n"
          "'Days of The week in Maori' or 'Numbers 1 - 10 in Maori\n"
          "After you choose you will get redirected to your chosen quiz"
          "You would have to write the displayed Day/Number in Maori/Te Reo\n"
          "\n"
          "After answering each question you will get told if you were right or wrong.\n"
          "Your final score would be displayed at the end of the quiz, and you can either try again or leave the program.\n"
          "\n"
          "Do you think you can get all the questions right?")
    print("-" * 50)
    print()


def quiz_chooser():
    choose_quiz = 0
    while choose_quiz == 0:
        # Ask the user if they want to continue to the quiz.
        print("0: Quit the Program\n"
              "1: Redirects to Days of the Week quiz\n"
              "2: Redirects to Numbers 1-10 quiz")
        choose_quiz = int(input("Choose one of the options above and press enter: "))
        print()

        # If the user inputs <enter>, output 'Program continues to quiz.
        if choose_quiz == 0:
            print(formatter("~", "Goodbye"))
            exit()

        # If the user inputs 'x', output 'You have quit the program', and a farewell message.
        elif choose_quiz == 1:
            score = 0
            total_score = days_of_week_quiz(score)
            print(f"Your total score was {total_score}/7")
            print()

        elif choose_quiz == 2:
            score = 0
            total_score = numbers_quiz(score)
            print(f"Your total score was {total_score}/10")
            print()

        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Please enter a valid answer. <enter> to play, or 'x' to quit.")
            choose_quiz = 0


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
        print()

        if user_answer == days[question_number][1]:
            player_score += 1
            print(formatter("=", "You are correct"))
            print()
        else:
            print(formatter("*", "You are incorrect"))
            print()

        # Adding 1 to the question number and the player score for every question
        question_number += 1

    # Returning users final score after all questions
    return player_score


def numbers_quiz(_quiz_score):
    player_score = 0
    question_number = 0
    # List of the days
    numbers = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
               [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]]
    random.shuffle(numbers)

    while question_number < 10:

        user_answer = input(f"What is the number {numbers[question_number][0]} in Maori: ").lower()
        print()

        if user_answer == numbers[question_number][1]:
            player_score += 1
            print(formatter("=", "You are correct"))
            print()
        else:
            print(formatter("*", "You are incorrect"))
            print()

        question_number += 1
    return player_score


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom} \n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("-", "Welcome to the Maori quiz"))
print()

tried_before = yes_no("Have you tried the quiz before? (Y for yes/N for No): ")
print()

if tried_before == "no":
    instructions()

play_again = ""

while play_again != "x":
    if play_again == "":
        quiz_chooser()
    else:
        print("Please enter a valid answer")
    play_again = input("Do you want to play again (<enter> to play, or 'x' to quit): ")
    print()
print(formatter("~", "Goodbye"))
