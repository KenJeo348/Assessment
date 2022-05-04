"""I made a new function which contains the instructions,
and linked it with the 01_yes_no_check_v3 function
to make a yes/no program working with the instructions.
"""


# Yes/No Function
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


# Instructions Function
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


# Main routine go here...
tried_before = yes_no("Have you tried the quiz before? (Y for yes/N for No): ")

if tried_before == "no":
    instructions()
else:
    print("Program continues")
