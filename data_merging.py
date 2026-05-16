import pandas as pd
import matplotlib.pyplot as plt

taxi_owners = pd.read_csv('taxi_owners.csv')
taxi_veh = pd.read_csv('taxi_vehicles.csv')


wards = pd.read_csv('Chicago_wards.csv')
census = pd.read_csv('Chicago_census.csv')
zip_demo = pd.read_csv('zip_demo.csv')
land_use = pd.read_csv('land_use.csv')

wards_altered = wards.copy()
census_altered = census.copy()


licenses = pd.read_csv('licenses.csv')
biz_owners = pd.read_csv('business_owners.csv')


cal = pd.read_csv('cta_calendar.csv')
ridership = pd.read_csv('cta_ridership.csv')
stations = pd.read_csv('stations.csv')


movies = pd.read_csv('movies.csv')
financials = pd.read_csv('financials.csv')
movies_genres = pd.read_csv('movie_to_genres.csv', index_col=0)
pop_movies = pd.read_csv('pop_movies.csv', index_col=0)

'''
create action and scifi movies tables by filtering the movies_genres 
table for the genres 'Action' and 'Science Fiction', respectively.

'''
# print(movies_genres.head())
scifi_movies = movies_genres[movies_genres['genre'] == 'Science Fiction'].reset_index(drop=True)
scifi_movies.to_csv('scifi_movies.csv')

action_movies = movies_genres[movies_genres['genre'] == 'Action'].reset_index(drop=True)
action_movies.to_csv('action_movies.csv')

'''
Different types of joins
inner join: returns only the rows that have matching values in both tables.
left join: returns all the rows from the left table, and the matched rows from the right
outer join: returns all the rows from both tables, with NaN in places where the join keys did not match.
right join: returns all the rows from the right table, and the matched rows from the left.
'''

'''
Inner Joins of tables.

Data Merging basically means combining two or more datasets into one. 
This is often done using a common key or identifier that exists in both datasets. 
In pandas, the merge() function is commonly used for this purpose.

When two DataFrames share column names that are not the one you are merging on, 
pandas automatically appends _x and _y to distinguish them. From the below code, 
to change those default endings to _own (for the left table, taxi_owners) and _veh (for the right table, taxi_veh).

add the suffixes parameter to your .merge() function, 
passing the two endings as a tuple: suffixes=('_own', '_veh')
'''

# Merge the taxi_owners and taxi_veh tables setting a suffix
# taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# print(taxi_own_veh.head())

# Print the value_counts to find the most popular fuel_type
# print(taxi_own_veh['fuel_type'].value_counts())


'''
Chicago wards and census data
'''
# print(wards['ward'].value_counts())

# Merge the wards and census tables on the ward column
# wards_census = wards.merge(census, on='ward')

# # Print the shape of wards_census
# print('wards_census table shape:', wards_census.shape)


# # Print the first few rows of the wards_altered table to view the change 
# print(wards_altered[['ward']].head())

# # Merge the wards_altered and census tables on the ward column
# wards_altered_census = wards_altered.merge(census, on='ward')

# # Print the shape of wards_altered_census
# print('wards_altered_census table shape:', wards_altered_census.shape)


# # Print the first few rows of the census_altered table to view the change 
# print(census_altered[['ward']].head())

# # Merge the wards and census_altered tables on the ward column
# wards_census_altered = wards.merge(census_altered, on = 'ward')

# # Print the shape of wards_census_altered
# print('wards_census_altered table shape:', wards_census_altered.shape)



# Merge the licenses and biz_owners table on account
# licenses_owners = licenses.merge(biz_owners, on = 'account')

# # Group the results by title then count the number of accounts
# counted_df = licenses_owners.groupby('title').agg({'account':'count'})
# # an alternative way to do the above is: 
# # counted_df = licenses_owners.groupby('title')['account'].count()

# # Sort the counted_df in descending order
# sorted_df = counted_df.sort_values('account', ascending = False)

# # Use .head() method to print the first few rows of sorted_df
# print(sorted_df.head())



'''
Merging Multiple DataFrames
You use on= when the matching column has the exact same name in both tables. Pandas finds it automatically in both.

left_on and right_on — when column names are different:
'''

# Merge the ridership, cal, and stations tables
# ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
# 							.merge(stations, on='station_id')

# # Create a filter to filter ridership_cal_stations
# filter_criteria = ((ridership_cal_stations['month'] == 7) 
#                    & (ridership_cal_stations['day_type'] == 'Weekday') 
#                    & (ridership_cal_stations['station_name'] == 'Wilson'))

# # Use .loc and the filter to select for rides
# print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())



# # Merge licenses and zip_demo, on zip; and merge the wards on ward
# licenses_zip_ward = licenses.merge(zip_demo, on = 'zip') \
#             			.merge(wards, on = 'ward')

# # Print the results by alderman and show median income
# print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))



# Merge land_use and census and merge result with licenses including suffixes
# land_cen_lic = land_use.merge(census, on='ward') \
#                     .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# # Group by ward, pop_2010, and vacant, then count the # of accounts
# pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
#                                    as_index=False).agg({'account':'count'})

# # Sort pop_vac_lic and print the results
# sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'], 
#                                              ascending= [False, True, False])

# # Print the top few rows of sorted_pop_vac_lic
# print(sorted_pop_vac_lic.head())




'''
left join
That's fantastic work! If your goal is to enhance or enrich a dataset, 
then you do not want to lose any of your original data. 
A left join will do that by returning all of the rows of your left table, 
while using an inner join may result in lost data if it does not exist in both tables.
'''

# Merge the movies table with the financials table with a left join
# movies_financials = movies.merge(financials, on='id', how='left')

# # Count the number of rows in the budget column that are missing
# number_of_missing_fin = movies_financials['budget'].isna().sum()

# # Print the number of movies missing financials
# print(number_of_missing_fin)


# # Merge action_movies to the scifi_movies with right join
# action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
#                                    suffixes=('_act','_sci'))

# # From action_scifi, select only the rows where the genre_act column is null
# scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# # Merge the movies and scifi_only tables with an inner join
# movies_and_scifi_only = movies.merge(scifi_only, left_on = 'id', right_on = 'movie_id')

# # Print the first few rows and shape of movies_and_scifi_only
# print(movies_and_scifi_only.head())
# print(movies_and_scifi_only.shape)


# Use right join to merge the movie_to_genres and pop_movies tables
# genres_movies = movies_genres.merge(pop_movies, how='right', 
#                                       right_on = 'id', 
#                                       left_on = 'movie_id')

# # Count the number of genres
# genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# # Plot a bar chart of the genre_count
# genre_count.plot(kind='bar')
# plt.show()



# # Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
# iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
#                                      on = 'id',
#                                      how = 'outer',
#                                      suffixes=('_1', '_2'))

# # Create an index that returns true if name_1 or name_2 are null
# m = ((iron_1_and_2['name_1'].isnull()) | 
#      (iron_1_and_2['name_2'].isnull()))

# # Print the first few rows of iron_1_and_2
# print(iron_1_and_2[m].head())



'''
merging a table to itself also known as self-join
'''


# employees = pd.DataFrame({
#     'employee_id': [1, 2, 3, 4, 5],
#     'name': ['Al-ameen', 'Salmat', 'John', 'Amina', 'Emeka'],
#     'manager_id': [3, 3, 5, 5, None]
# })

# print(employees)

# self_joined = employees.merge( #LEFT copy of the table
#     employees,                 #RIGHT copy of the table 
#     left_on='manager_id',
#     right_on='employee_id',
#     suffixes=('_employee', '_manager')
# )

# print(self_joined[['name_employee', 'name_manager']])



# products = pd.DataFrame({
#     'Product': ['Rice', 'Beans', 'Garri', 'Yam'],
#     'Price': [45000, 32000, 18000, 25000]
# })

# stock = pd.DataFrame({
#     'Product': ['Rice', 'Beans', 'Plantain'],
#     'Stock': [100, 50, 200]
# })

# print("INNER:")
# print(pd.merge(products, stock, on='Product', how='inner'))

# print("\nLEFT:")
# print(pd.merge(products, stock, on='Product', how='left'))

# print("\nOUTER:")
# print(pd.merge(products, stock, on='Product', how='outer'))

'''
Advanced Merging and Concatenating
Semi Join — keep only rows from the left table that have a match in the right table:

Anti Join — keep only rows from the left table that have NO match in the right table:

Filtering join is actually just the category name that covers both semi join and anti join. 
They're called filtering joins because instead of combining columns from both tables — 
they simply filter the left table based on whether a match exists in the right table.

Regular joins → combine columns from both tables
Filtering joins → only filter rows, keep only left table columns
'''

# products = pd.DataFrame({
#     'Product': ['Rice', 'Beans', 'Garri', 'Yam'],
#     'Price': [45000, 32000, 18000, 25000]
# })

# stock = pd.DataFrame({
#     'Product': ['Rice', 'Beans', 'Plantain'],
#     'Stock': [100, 50, 200]
# })


# # semi join
# semi_join = products[products['Product'].isin(stock['Product'])]
# print(semi_join)

# # anti join
# anti_join = products[~products['Product'].isin(stock['Product'])]
# print(anti_join)


# registered = pd.DataFrame({
#     'Name': ['Al-ameen', 'Salmat', 'John', 'Amina', 'Emeka'],
#     'LGA': ['Lagos', 'Abuja', 'Kano', 'Lagos', 'PH']
# })

# voted = pd.DataFrame({
#     'Name': ['Al-ameen', 'John', 'Emeka'],
#     'Voted': [True, True, True]
# })

# # semi join - who voted
# voted_voters = registered[registered['Name'].isin(voted['Name'])]
# print("Voted:")
# print(voted_voters)

# # anti join - who didn't vote
# didnt_vote = registered[~registered['Name'].isin(voted['Name'])]
# print("\nDidn't vote:")
# print(didnt_vote)



'''
Concatenation
'''
# Concatenate the tracks
import pandas as pd
import matplotlib.pyplot as plt

# Create three months of Nigerian sales data
sales_jan = pd.DataFrame({
    'product': ['Rice', 'Beans', 'Garri'],
    'total': [45000, 32000, 18000]
})

sales_feb = pd.DataFrame({
    'product': ['Yam', 'Plantain', 'Rice'],
    'total': [25000, 8000, 42000]
})

sales_mar = pd.DataFrame({
    'product': ['Beans', 'Garri', 'Yam'],
    'total': [30000, 20000, 28000]
})

# Concatenate the tables and add month keys
sales_jan_thr_mar = pd.concat([sales_jan, sales_feb, sales_mar],
                               keys=['1Jan', '2Feb', '3Mar'])

print("Combined sales data:")
print(sales_jan_thr_mar)

# Group by month and find average total sales per month
avg_sales_by_month = sales_jan_thr_mar.groupby(level=0).agg({'total': 'mean'})

print("\nAverage sales per month:")
print(avg_sales_by_month)

# Bar plot of average sales by month
avg_sales_by_month.plot(kind='bar')
plt.title('Average Monthly Sales - Nigerian Market')
plt.xlabel('Month')
plt.ylabel('Average Sales (NGN)')
plt.tight_layout()
plt.show()