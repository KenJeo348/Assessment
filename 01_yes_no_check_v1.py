# Ask the user if the have played before
yes_no = input("Have you tried the quiz before? (Y for yes/N for No):").lower()

# If they say yes, output 'Program Continues'
if yes_no == "y":
    print("Program Continues")

# If they say no, output 'Display Instructions'
elif yes_no == "n":
    print("Display Instructions")

# Otherwise - show error message
else:
    print("Please enter either Y/N.")
