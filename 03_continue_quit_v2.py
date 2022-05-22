""" Code turned into a while Loop for more convenient testing
and looping if user doesn't enter <enter> , or 'x'
based on 03_continue_quit_v1
"""

continue_or_quit = ""

while continue_or_quit != "x":
    # Ask the user if they want to continue to the quiz.
    continue_or_quit = input("Do you want to continue to the quiz? <enter> to play or 'x' to quit:").lower()

    # If the user inputs <enter>, output 'Program continues to quiz.
    if continue_or_quit == "":
        print("Program continues to quiz.")

    # If the user inputs 'x', output 'You have quit the program', and a farewell message.
    elif continue_or_quit == "x":
        print("You have quit the program.\n"
              "We hope we could see you again.")

    # If the user enters an invalid answer, output 'Please enter a valid answer'
    else:
        print("Please enter a valid answer. <enter> to play, or 'x' to quit.")


