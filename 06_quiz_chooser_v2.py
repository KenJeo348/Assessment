""" Based on 06_quiz_chooser_v1 modified so that it would work for
inputs that are value errors such as strings."""


def quiz_chooser():
    valid = False
    while not valid:
        try:
            # Ask the user if they want to continue to the quiz.
            print("0: Quit the Program\n"
                  "1: Redirects to Days of the Week quiz\n"
                  "2: Redirects to Numbers 1-10 quiz")
            choose_quiz = int(input("Choose one of the options above and press enter: "))

            # If the user inputs 0, exit the program
            if choose_quiz == 0:
                exit()

            # If the user inputs 1, print 'Redirect to days of the week quiz'.
            elif choose_quiz == 1:
                print("Redirect to days of the week quiz")
                valid = True

            # If the user inputs 2, print 'Redirect to Numbers 1-10 quiz'.
            elif choose_quiz == 2:
                print("Redirect to Numbers 1-10 quiz")
                valid = True

            # If the user enters an invalid answer, output 'Please enter a valid answer'
            else:
                print("Please enter a valid answer. <enter> to play, or 'x' to quit.")

        # If the user inputted a Value error, such as a string, output 'Please enter a valid answer'
        except ValueError:
            print("Please enter a valid answer. <enter> to play, or 'x' to qo quit")


# Main routine
quiz_chooser()
print("Code finished")
