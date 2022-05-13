# Code from 03_continue_quit_v2 turned into a function.


def quiz_chooser():
    choose_quiz = 0
    valid = False
    while not valid:
        try:
            # Ask the user if they want to continue to the quiz.
            print("0: Quit the Program\n"
                  "1: Redirects to Days of the Week quiz\n"
                  "2: Redirects to Numbers 1-10 quiz")
            choose_quiz = int(input("Choose one of the options above and press enter: "))

            # If the user inputs <enter>, output 'Program continues to quiz.
            if choose_quiz == 0:
                exit()

            # If the user inputs 'x', output 'You have quit the program', and a farewell message.
            elif choose_quiz == 1:
                print("Redirect to days of the week quiz")
                valid = True

            elif choose_quiz == 2:
                print("Redirect to Numbers 1-10 quiz")
                valid = True

            # If the user enters an invalid answer, output 'Please enter a valid answer'
            else:
                print("Please enter a valid answer. <enter> to play, or 'x' to quit.")

        except ValueError:
            print("Please enter a valid answer. <enter> to play, or 'x' to qo quit")


# Main routine
quiz_chooser()
print("Code finished")
