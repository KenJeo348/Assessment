"""Component 5 (Numbers 1-10 quiz)
Generate the numbers from 1-10 in a random order
"""

import random
# List of the days
days = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
        [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]]

# Mixing the list in a random order
random.shuffle(days)

# Printing mixed list.
print(days)
