"""Component 4 (Days of the week quiz)
Generate the numbers from 1-10 in a random order
"""

import random
# List of the days
days = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"],
        [7, "whitu"], [8, "waru"], [9, "iwa"], [10, "tekau"]]
random.shuffle(days)
print(days)
