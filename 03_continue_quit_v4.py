"""Code has been changed so that it gives the user a choice
of which quiz to go to or quit.
Based on 03_continue_quit_v3"""


def continue_or_quit_function():
    continue_or_quit = "Starting Text"
    while continue_or_quit != 0:
        # Ask the user if they want to continue to the quiz.
        print("0: Quit the Program\n"
              "1: Redirects to Days of the Week quiz\n"
              "2: Redirects to Numbers 1-10 quiz")
        continue_or_quit = int(input("Choose one of the options above and enter:"))

        # If the user inputs 0, output 'User has quit the program, then quit.
        if continue_or_quit == 0:
            print("User has quit the program. ")

            exit()
        # If the user inputs 1, output 'Program Continues to days of the week quiz'.
        elif continue_or_quit == 1:
            print("Program Continues to days of the week quiz.")
            break

        # if the user inputs 2, output 'Program Continues to Numbers 1-10 quiz'.
        elif continue_or_quit == 2:
            print("Program Continues to Numbers 1-10 quiz.")
            break

        # If the user enters an invalid answer, output 'Please enter a valid answer'
        else:
            print("Please enter a valid answer. <enter> to play, or 'x' to quit.")


# Main routine
continue_or_quit_function()
