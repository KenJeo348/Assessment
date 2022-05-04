# Code from 03_continue_quit_v2 turned into a function.


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
continue_or_quit_function()
