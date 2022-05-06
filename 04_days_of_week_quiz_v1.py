"""Component 4 (Days of the week quiz)
Generate the days of the week in a random order
"""

import random
# List of the days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
random.shuffle(days)
print(days)
