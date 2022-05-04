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
    continue_or_quit = "start"
    while continue_or_quit != "":
        # Ask the user if they want to continue to the quiz.
        continue_or_quit = input("Do you want to continue to the quiz? <enter> to play or 'x' to quit:").lower()

        # If the user inputs <enter>, output 'Program continues to quiz.
        if continue_or_quit == "":
            print("Program continues to quiz.")

        # If the user inputs 'x', output 'You have quit the program', and a farewell message.
        elif continue_or_quit == "x":

            print("You have quit the program.\n"
                  "We hope we could see you again.")
            exit()
        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Please enter a valid answer. <enter> to play, or 'x' to quit.")


# Main routine
tried_before = yes_no("Have you tried the quiz before? (Y for yes/N for No): ")

if tried_before == "no":
    instructions()

else:
    continue_or_quit_function()

continue_or_quit_function()
