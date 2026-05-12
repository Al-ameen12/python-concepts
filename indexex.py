import pandas as pd

temperatures = pd.read_csv('temperatures.csv', index_col=0)


# # Force pandas to show all rows and columns in the CLI
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# # Optional: Prevent text from wrapping to a new line if the table is wide
# pd.set_option('display.width', 1000)

# # Look at temperatures
print(temperatures.head())

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
# print(temperatures_ind.sort_index())

# # Sort temperatures_ind by index values at the city level
# print(temperatures_ind.sort_index(level = "city"))

# # Sort temperatures_ind by country then descending city
# print(temperatures_ind.sort_index(level= ["country", "city"], ascending = [True, False]))

'''
Slicing index values
'''
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Philippines
# print(temperatures_srt.loc["Pakistan":"Philippines"])

# Try to subset rows from Lahore to Manila
# print(temperatures_srt.loc["Lahore":"Manila"])

# Subset rows from Pakistan, Lahore to Philippines, Manila
# print(temperatures_srt.loc[("Pakistan","Lahore"):("Philippines","Manila")])

'''
Slicing in both directions
'''

# # Subset rows from India, Hyderabad to Iraq, Baghdad
# print(temperatures_srt.loc[("India", "Hyderabad") : ("Iraq", "Baghdad")])

# # Subset columns from date to avg_temp_c
# print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# # Subset in both directions at once
# print(temperatures_srt.loc[("India", "Hyderabad") : ("Iraq", "Baghdad"), "date":"avg_temp_c"])

'''
Slicing time series
'''

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
# temperatures_bool = temperatures[(temperatures['date'] >= "2010-01-01") & (temperatures['date'] <= '2011-12-31')]
# print(temperatures_bool)

# # Set date as the index and sort the index
# temperatures_ind = temperatures.set_index('date').sort_index()

# # Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
# print(temperatures_ind.loc["2010" : "2011"])

# # Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
# print(temperatures_ind.loc["2010-08" : "2011-02"])


'''
Subsetting by row/column number
This is done using .iloc[], and like .loc[], 
it can take two arguments to let you subset by rows and columns.
'''
# Get 23rd row, 2nd column (index 22, 1)
# print(temperatures.iloc[22, 1])

# # Use slicing to get the first 5 rows
# print(temperatures.iloc[:5])

# # Use slicing to get columns 3 to 4
# print(temperatures.iloc[:, 2:4])

# # Use slicing in both directions at once
# print(temperatures.iloc[:5, 2:4])

'''
Pivot tables
'''
# Convert the date column to datetime objects
temperatures['date'] = pd.to_datetime(temperatures['date'])

# Add a year column to temperatures
temperatures['year'] = temperatures['date'].dt.year
# print(temperatures.head())

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values = 'avg_temp_c', index = ['country', 'city'], columns = 'year')

# See the result
print(temp_by_country_city_vs_year)