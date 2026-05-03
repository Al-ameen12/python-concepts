'''
Regular for loop on a 2D array → gives you one row at a time
np.nditer() → gives you one element at a time regardless of shape
'''
import pandas as pd
import numpy as np

# 1D array
# heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])

# for height in heights:
#     print(height)


# data = np.array([[1.73, 65.4],
#                  [1.68, 59.2],
#                  [1.71, 63.6]])

# # looping over 2D array normally
# for row in data:
#     print(row)


# looping over every single element
# for element in np.nditer(data):
#     print(element)


# looping over Pandas DataFrame

# data = {
#     'Name': ['Al-ameen', 'Sarah', 'John', 'Amina'],
#     'Score': [96, 78, 62, 91],
#     'City': ['Lagos', 'Abuja', 'Kano', 'Lagos']
# }

# df = pd.DataFrame(data)

# for row in df:
#     print(row)

# for index, row in df.iterrows():
#     # print(index, row)
#     print(index, row)


# for index, row in df.iterrows():
#     print(f"Student {index}: {row['Name']} scored {row['Score']} and is from {row['City']}")

# for index, row in df.iterrows():
#     if row['Score'] >= 70:
#         grade = 'Pass'
#     else:
#         grade = 'Fail'
#     print(f"{row['Name']}: {row['Score']} - {grade}")

# Adding a new column using iterrows()


# data = {
#     'Name': ['Al-ameen', 'Sarah', 'John', 'Amina'],
#     'Score': [95, 78, 62, 51],
#     'City': ['Lagos', 'Abuja', 'Kano', 'Lagos']
# }

# df = pd.DataFrame(data)

# # adding grade column using iterrows()
# for index, row in df.iterrows():
#     if row['Score'] >= 70:
#         df.loc[index, 'Grade'] = 'Pass'
#     else:
#         df.loc[index, 'Grade'] = 'Fail'

# print(df)


# data = {
#     'Name': ['Al-ameen', 'Sarah', 'John', 'Amina'],
#     'Score': [95, 78, 62, 91],
#     'City': ['Lagos', 'Abuja', 'Kano', 'Lagos']
# }

# df = pd.DataFrame(data)

# # loc - using labels
# print(df.loc[0, 'Name'])       # row 0, Name column
# print(df.loc[1:3, 'Name':'City']) # rows 1-3, Name to City columns

# # iloc - using position numbers
# print(df.iloc[0, 0])           # row 0, column 0
# print(df.iloc[1:3, 0:2])       # rows 1-3, columns 0-2

# data = {
#     'Product': ['Rice', 'Beans', 'Garri', 'Yam'],
#     'Price': [45000, 32000, 18000, 25000],
#     'City': ['Lagos', 'Abuja', 'Kano', 'Lagos']
# }
# df = pd.DataFrame(data)

# print(df.loc[2, 'Price'])
# print(df.iloc[0:2, 0])

'''
WHEN NOT TO USE ITERROWS()

Use iterrows() — when you need to access multiple columns per row
Use apply() — when you're working on a single column
'''

data = {
    'Name': ['Al-ameen', 'Sarah', 'John', 'Amina'],
    'Score': [45, 78, 62, 91],
    'City': ['Lagos', 'Abuja', 'Kano', 'Lagos']
}

df = pd.DataFrame(data)

# instead of iterrows() use apply()
def assign_grade(score):
    if score >= 70:
        return 'Pass'
    else:
        return 'Fail'

df['Grade'] = df['Score'].apply(assign_grade)
print(df)