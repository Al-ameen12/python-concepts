'''
Matplotlib is Python's most popular data visualization library. 
It turns numbers into charts and graphs you can actually see and interpret.

for lineplot:
plt.plot(cities, populations)
for bar chart:
plt.bar(cities, populations)
for scatter plot:
plt.scatter(cities, populations)

Histogram — shows distribution of data:
Scatter plot — shows relationship between two variables:


fig, axes = plt.subplots(1, 3, figsize=(15, 5))
This returns two things simultaneously:

fig — the entire figure/window containing all plots
axes — a list of the 3 individual plot canvases
figsize=(15, 5) — sets the window size. 15 wide, 5 tall in inches.
plt.subplots() — creates a grid of subplots. Here, 1 row and 3 columns.
axes[0] — the first subplot (bar chart)
axes[1] — the second subplot (histogram)
axes[2] — the third subplot (scatter plot)
'''
# import matplotlib.pyplot as plt

# Nigerian cities and their populations in millions
# cities = ['Lagos', 'Kano', 'Ibadan', 'Abuja', 'Port Harcourt']
# populations = [15.9, 4.1, 3.6, 3.3, 2.5]

# plt.scatter(cities, populations, color="black")
# plt.title('Nigerian City Populations')
# plt.xlabel('City')
# plt.ylabel('Population (millions)')
# plt.show()

# Histogram of the populations
# import matplotlib.pyplot as plt
# import numpy as np

# ages = np.random.randint(18, 45, 50)

# plt.hist(ages, bins=10, color='blue', edgecolor='black')
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

# import matplotlib.pyplot as plt

# study_hours = [2, 4, 6, 8, 10, 12, 14]
# test_scores = [45, 55, 65, 70, 80, 88, 95]

# plt.scatter(study_hours, test_scores, color='red')
# plt.title('Study Hours vs Test Scores')
# plt.xlabel('Hours Studied')
# plt.ylabel('Score')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

students = np.array([45, 78, 62, 91, 55, 83, 72, 66, 88, 59])

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].bar(range(1, 11), students, color='green')
axes[0].set_title('Student Scores')
axes[0].set_xlabel('Student')
axes[0].set_ylabel('Score')

axes[1].hist(students, bins=5, color='blue', edgecolor='black')
axes[1].set_title('Score Distribution')
axes[1].set_xlabel('Score Range')
axes[1].set_ylabel('Frequency')

axes[2].scatter(range(1, 11), students, color='red')
axes[2].set_title('Score Pattern')
axes[2].set_xlabel('Student')
axes[2].set_ylabel('Score')

plt.suptitle('Nigerian Student Performance Analysis')
plt.tight_layout()
plt.show()