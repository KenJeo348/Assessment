"""Component 4 (Days of the week quiz)
Generate the days of the week in a random order
"""

import random
# List of the days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Mixing the list into a random order.
random.shuffle(days)

# Printing the list.
print(days)
