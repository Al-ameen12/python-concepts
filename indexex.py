import pandas as pd

temperatures = pd.read_csv('temperatures.csv', index_col=0)

# # Look at temperatures
# # print(temperatures)

# # Set the index of temperatures to city
# temperatures_ind = temperatures.set_index('city')

# # Look at temperatures_ind
# # print(temperatures_ind)

# # Reset the temperatures_ind index, keeping its contents
# # print(temperatures_ind.reset_index())

# # Reset the temperatures_ind index, dropping its contents
# print(temperatures_ind.reset_index(drop=True))


'''
Subsetting with .loc[]
The .loc[] property stands for "location by label." 
Its only job is to look at the row labels (the index 
column on the far left) and pull rows that match the 
exact label you pass to it.
'''

# Make a list of cities to subset on
# cities = ["London", "Paris"]

# Subset temperatures using square brackets
# print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
# print(temperatures_ind.loc[cities])


'''
setting multi-level index
'''
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])


'''
Sorting by index values
'''
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level = "city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level= ["country", "city"], ascending = [True, False]))