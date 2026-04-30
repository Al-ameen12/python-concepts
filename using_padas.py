'''
codes/notes from datacamp

Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python. Sounds promising!

The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data where you can label the rows and the columns. One way to build a DataFrame is from a dictionary.

In the exercises that follow you will be working with vehicle data from different countries. Each observation corresponds to a country and the columns give information about the number of vehicles per capita, whether people drive left or right, and so on.

Three lists are defined in the script:

    names, containing the country names for which data is available.
    dr, a list with booleans that tells whether people drive left or right in the corresponding country.
    cpc, the number of motor vehicles per 1000 people in the corresponding country.

Each dictionary key is a column label and each value is a list which contains the column elements.


iloc: The iloc indexer for Pandas Dataframe is used for integer-location based indexing / selection by position. It is used to select rows and columns by number
loc: The loc indexer for Pandas Dataframe is used for label-location based indexing / selection by label. It is used to select rows and columns by label.

square brackets [] are used to select columns from a DataFrame. You can also use them to select rows, but this is not recommended. Instead, you should use the loc and iloc indexers.



Questions:
how is the indext from the output generated? is it just the position of the row in the original list? or is it something else?
'''

# # Pre-defined lists
# names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
# dr =  [True, False, False, False, True, True, True]
# cpc = [809, 731, 588, 18, 200, 70, 45]

# # Import pandas as pd
# import pandas as pd

# # Create dictionary my_dict with three key:value pairs: my_dict
# my_dict = {'country' : names,
#             'drives_right' : dr,
#             'cars_per_cap' : cpc}

# # Build a DataFrame cars from my_dict: cars
# cars = pd.DataFrame(my_dict)

# # Print cars
# print(cars)

'''
What is Pandas?
Pandas is Python's most powerful data analysis library. If NumPy is about numerical computing, Pandas is about working with structured data — think Excel spreadsheets but in Python, faster and more powerful.

The two core data structures:

Series — a single column of data (1D)
DataFrame — a full table with rows and columns (2D)

pd.Series() creates a one-dimensional labeled array — think of it as a single column in a spreadsheet.
It takes two things:

The data — [45, 78, 62, 91, 55]
The index — ['Al-ameen', 'Sara', 'John', 'Amina', 'Emeka']

The index is simply the label for each value — like row names.
Without a custom index Pandas automatically assigns numbers 0, 1, 2, 3...

Why int64 and not just int?
Regular Python int can store any size number — it's flexible but slow.
int64 is a NumPy integer that uses exactly 64 bits of memory — it's fixed in size which makes it significantly faster for large datasets.
The 64 refers to how many bits are used to store the number. You'll also see:


'''
import pandas as pd

# scores = pd.Series([45, 78, 62, 91, 55], 
#                    index=['Al-ameen', 'Sara', 'Hassan', 'Lina', 'Omar'])
# print(scores)
# print(type(scores))

# DataFrame
# data = {
#     'Name': ['Al-ameen', 'Sara', 'John', 'Amina', 'Emeka'],
#     'Score': (45, 78, 62, 91, 55),
#     'City': ['Lagos', 'Abuja', 'Kano', 'Lagos', 'PH']
# }

# df = pd.DataFrame(data)
# print(df)

# Pandas operations:
# print(df.head())      # first 5 rows
# print(df.tail())      # last 5 rows
# print(df.shape)       # rows and columns count
# print(df.info())      # data types and missing values
# print(df.describe())  # statistical summary

# selecting data:
# select one column
# print(df['Name'])

# # select multiple columns
# print(df[['Name', 'Score']])

# # select rows by condition
# print(df[df['Score'] > 60])


# adding, updating and removing data:
# adding a new column
# df['Grade'] = ['F', 'B', 'C', 'A', 'F']
# print(df)

# # updating a value
# df.loc[0, 'Score'] = 75
# print(df)

# # removing a column
# df = df.drop('Grade', axis=1)
# print(df)


# working with real data from a file:
# create an empty csv file

# data = {
#     'Product': ['Rice', 'Beans', 'Garri', 'Yam', 'Plantain'],
#     'Price': [45000, 32000, 18000, 25000, 8000],
#     'City': ['Lagos', 'Abuja', 'Kano', 'Lagos', 'PH']
# }

# df = pd.DataFrame(data)
# df.to_csv('nigerian_prices.csv', index=False)
# print("File saved")

# # now read it back
# df2 = pd.read_csv('nigerian_prices.csv')
# print(df2)


# analysis on that Nigerian prices data:

df = pd.read_csv('nigerian_prices.csv')

# most expensive product
print("Most expensive:", df.loc[df['Price'].idxmax(), 'Product'])

# cheapest product
print("Cheapest:", df.loc[df['Price'].idxmin(), 'Product'])

# average price
print("Average price:", df['Price'].mean())

# products above average price
avg = df['Price'].mean()
print("\nAbove average price:")
print(df[df['Price'] > avg])

# total value of all products
print("\nTotal market value:", df['Price'].sum())


# Filtering Data using pandas
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']
# print(dr)

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

'''
to be uploaded to csv file later
 cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JPN           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True
     cars_per_cap        country  drives_right
US            809  United States          True
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True
'''

# using  logical operation with pandas and numpy
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)