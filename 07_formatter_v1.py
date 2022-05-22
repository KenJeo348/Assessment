"""Component 7
Statement Formatter
"""

# Symbol surrounding chosen text.
symbol = "*"

# Chosen Text
text = "hello world"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

# Output
print(top_bottom)
print(formatted_text)
print(top_bottom)
