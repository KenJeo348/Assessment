# Code from 03_continue_quit_v2 turned into a function.


def continue_or_quit_function():
    continue_or_quit = "Starting Text"
    while continue_or_quit != 0:
        # Ask the user if they want to continue to the quiz.
        print("0: Quit the Program\n"
              "1: Redirects to Days of the Week quiz\n"
              "2: Redirects to Numbers 1-10 quiz")
        continue_or_quit = int(input("Choose one of the options above and enter:"))

        # If the user inputs <enter>, output 'Program continues to quiz.
        if continue_or_quit == 0:
            print("User has quit the program. ")

            exit()

        elif continue_or_quit == 1:
            print("Program Continues to days of the week quiz.")
            break

        # If the user inputs 'x', output 'You have quit the program', and a farewell message.
        elif continue_or_quit == 2:
            print("Program Continues to Numbers 1-10 quiz.")
            break

        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Please enter a valid answer. <enter> to play, or 'x' to quit.")


# Main routine
continue_or_quit_function()
