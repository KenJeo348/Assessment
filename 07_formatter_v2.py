"""Component 5 - statement formatter v2
Change v1 into a function
"""


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom} \n{formatted_text}\n{top_bottom}"


# main routine
text_ = input("Enter the statement you want to format: ")
symbol_ = input("What symbol do you want to use: ")
print()
print(formatter(symbol_, text_))

