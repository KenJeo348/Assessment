"""Temporary While loop used for more convenient testing.
Based on 01_yes_no_check_v1"""

yes_no = ""
while yes_no != "stop testing":
    # Ask the user if the have played before
    yes_no = input("Have you tried the quiz before? (Y for yes/N for No): ").lower()

    # If they say yes, output 'Program Continues'
    if yes_no == "y" or yes_no == "yes":
        print("Program Continues")

    # If they say no, output 'Display Instructions'
    elif yes_no == "n" or yes_no == "no":
        print("Display Instructions")

    # Otherwise - show error
    else:
        print("Please enter either Y/N.")
