"""Yes/No Checking function
based on 01_yes_no_check_v2
"""


# Function goes here...
def yes_no(question_text):
    while True:

        # Ask the user if the have played before
        answer = input(question_text).lower()

        # If they say yes, return Yes
        if answer == "" or answer == "yes":
            answer = "yes"
            return answer

        # If they say no, return No
        elif answer == "n" or answer == "no":
            answer = "no"
            return answer

        # Otherwise - show error
        else:
            print("Please enter either Y/N or Yes/No")


# Main routine go here...
tried_before = yes_no("Have you tried the quiz before? (Y for yes/N for No): ")
print(f"You entered {tried_before}")

