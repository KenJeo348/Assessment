"""Component 5 - statement formatter v3
Call function 3 times - once for each of the tests
"""


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom} \n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("-", "Welcome to the Maori quiz"))
print()
print(formatter("~", "Goodbye"))
print()
print(formatter("=", "Correct"))
print()
print(formatter("*", "Incorrect"))

