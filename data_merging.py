import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
# # Concatenate the tracks
# import pandas as pd
# import matplotlib.pyplot as plt

# # Create three months of Nigerian sales data
# sales_jan = pd.DataFrame({
#     'product': ['Rice', 'Beans', 'Garri'],
#     'total': [45000, 32000, 18000]
# })

# sales_feb = pd.DataFrame({
#     'product': ['Yam', 'Plantain', 'Rice'],
#     'total': [25000, 8000, 42000]
# })

# sales_mar = pd.DataFrame({
#     'product': ['Beans', 'Garri', 'Yam'],
#     'total': [30000, 20000, 28000]
# })

# # Concatenate the tables and add month keys
# sales_jan_thr_mar = pd.concat([sales_jan, sales_feb, sales_mar],
#                                keys=['1Jan', '2Feb', '3Mar'])

# print("Combined sales data:")
# print(sales_jan_thr_mar)

# # Group by month and find average total sales per month
# avg_sales_by_month = sales_jan_thr_mar.groupby(level=0).agg({'total': 'mean'})

# print("\nAverage sales per month:")
# print(avg_sales_by_month)

# # Bar plot of average sales by month
# avg_sales_by_month.plot(kind='bar')
# plt.title('Average Monthly Sales - Nigerian Market')
# plt.xlabel('Month')
# plt.ylabel('Average Sales (NGN)')
# plt.tight_layout()
# plt.show()



'''
Why merge_ordered() instead of regular merge():
merge_ordered() is specifically designed for time series data — 
it keeps the data sorted by date automatically and supports fill methods like ffill. 
Regular merge() doesn't have that capability.

forward fill: fill_method='ffill'
'''

# # GDP data - reported yearly
# gdp = pd.DataFrame({
#     'year': [2018, 2019, 2020, 2021, 2022],
#     'gdp': [20500, 21400, 20900, 23000, 25500]
# })

# # S&P500 data - reported by date
# sp500 = pd.DataFrame({
#     'date': [2018, 2019, 2020, 2021, 2022],
#     'returns': [0.12, 0.28, 0.16, 0.27, -0.19]
# })

# # Use merge_ordered() to merge gdp and sp500, and forward fill missing values
# gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date',
#                              how='left', fill_method='ffill')

# # Subset the gdp and returns columns
# gdp_returns = gdp_sp500[['gdp', 'returns']]

# print("Merged table:")
# print(gdp_sp500)

# print("\nCorrelation:")
# print(gdp_returns.corr())

'''
Generating a large sample dataset

Different numpy function here — randint instead of uniform:

uniform — generates decimal numbers
randint — generates whole numbers only


pd.DatetimeIndex() converts the date column into a datetime object 
that has a .year attribute you can extract.
'''

# Generate large sample dataset
# np.random.seed(42)
# dates = pd.date_range(start='2010-01-01', end='2023-12-01', freq='MS')

# # Inflation dataset - Consumer Price Index
# inflation = pd.DataFrame({
#     'date': dates,
#     'cpi': np.random.uniform(200, 320, len(dates)).round(2),
#     'inflation_rate': np.random.uniform(1.5, 9.5, len(dates)).round(2)
# })

# # Unemployment dataset
# unemployment = pd.DataFrame({
#     'date': dates,
#     'unemployment_rate': np.random.uniform(3.5, 14.5, len(dates)).round(2),
#     'job_openings': np.random.randint(5000000, 12000000, len(dates))
# })

# # # Use merge_ordered() to merge inflation and unemployment with inner join
# inflation_unemploy = pd.merge_ordered(inflation, unemployment,
#                                       how='inner', on='date')

# # Print first 10 rows
# print("Merged table (first 10 rows):")
# print(inflation_unemploy.head(10))

# Print shape
# print(f"\nDataset shape: {inflation_unemploy.shape}")

# # Print correlation
# print("\nCorrelation matrix:")
# print(inflation_unemploy[['cpi', 'inflation_rate', 
#                            'unemployment_rate', 'job_openings']].corr())

# # Plot scatter plot of unemployment_rate vs cpi
# inflation_unemploy.plot(x='unemployment_rate', y='cpi', kind='scatter',
#                         color='red', alpha=0.5)
# plt.title('Unemployment Rate vs CPI (2010-2023)')
# plt.xlabel('Unemployment Rate (%)')
# plt.ylabel('Consumer Price Index')
# plt.tight_layout()
# plt.show()

# # Plot scatter plot of inflation_rate vs unemployment_rate
# inflation_unemploy.plot(x='unemployment_rate', y='inflation_rate', 
#                         kind='scatter', color='blue', alpha=0.5)
# plt.title('Unemployment Rate vs Inflation Rate (2010-2023)')
# plt.xlabel('Unemployment Rate (%)')
# plt.ylabel('Inflation Rate (%)')
# plt.tight_layout()
# plt.show()

# Average CPI and unemployment per year
# inflation_unemploy['year'] = pd.DatetimeIndex(inflation_unemploy['date']).year
# yearly_avg = inflation_unemploy.groupby('year').agg({
#     'cpi': 'mean',
#     'inflation_rate': 'mean',
#     'unemployment_rate': 'mean'
# }).round(2)

# print("\nYearly averages:")
# print(yearly_avg)

# # Bar plot of yearly average unemployment
# yearly_avg['unemployment_rate'].plot(kind='bar', color='green')
# plt.title('Average Yearly Unemployment Rate (2010-2023)')
# plt.xlabel('Year')
# plt.ylabel('Unemployment Rate (%)')
# plt.tight_layout()
# plt.show()

'''
Demonstrate forward fill by Generating large Dataset with missing values

OBSERVATIONS:
Before merge — GDP table has 8 rows, population table has 6 rows. Population is missing some country/date combinations deliberately.
After merge — notice rows where population was missing. fill_method='ffill' carries the last known population value forward to fill those gaps.
The correlation — tells you whether larger population countries tend to have larger GDP in this dataset.


ABOUT np.random.seed(42)
Setting a random seed is a common practice in data science and machine learning to ensure reproducibility of results. 
When you generate random numbers, they are typically based on an algorithm that produces a sequence of numbers that appear random. 
By setting a specific seed value (in this case, 42), you ensure that the same sequence of random numbers is generated each time you run the code. 
This is particularly useful when you want to share your code with others or when you want to debug your code, as it allows you to get the same results consistently.
'''
# Generate sample data
# np.random.seed(42)

# countries = ['Nigeria', 'Ghana', 'Kenya', 'Egypt']
# dates = [2019, 2020, 2021, 2022]

# # GDP dataset
# gdp = pd.DataFrame({
#     'date': [2019, 2019, 2020, 2020, 2021, 2021, 2022, 2022],
#     'country': ['Nigeria', 'Ghana', 'Nigeria', 'Ghana', 
#                 'Nigeria', 'Ghana', 'Nigeria', 'Ghana'],
#     'gdp_billions': np.random.uniform(50, 500, 8).round(2)
# })

# # Population dataset - notice missing rows to demonstrate ffill
# pop = pd.DataFrame({
#     'date': [2019, 2019, 2020, 2021, 2022, 2022],
#     'country': ['Nigeria', 'Ghana', 'Nigeria', 'Nigeria', 
#                 'Nigeria', 'Ghana'],
#     'population_millions': np.random.uniform(10, 220, 6).round(2)
# })

# # print("GDP table:")
# # print(gdp)

# # print("\nPopulation table:")
# # print(pop)

# # # Merge gdp and pop on date and country with forward fill
# ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'],
#                              fill_method='ffill')

# # # Print ctry_date
# print("\nMerged table:")
# print(ctry_date)

# # # Check correlation between gdp and population
# print("\nCorrelation:")
# print(ctry_date[['gdp_billions', 'population_millions']].corr())



'''
Using merge_asof() to study stocks
What merge_asof() actually does:
It merges two tables based on the nearest matching key — not exact matches. 
The keys must be sorted before merging.
Think of it like this — you have stock prices recorded at slightly different times for different banks. 
merge_asof() says "match each JPMorgan timestamp to the closest Wells Fargo timestamp" 
rather than requiring exact time matches.

What direction='nearest' means:
Matches to the closest timestamp in either direction — before or after. 
That's why it worked — it's the most flexible option.
'''

# Generate stock price data for three Nigerian banks
# np.random.seed(42)

# # Access Bank stock prices
# access_times = pd.date_range(start='2023-01-01 09:00:00', 
#                              periods=10, freq='1min')
# access = pd.DataFrame({
#     'date_time': access_times,
#     'close': np.random.uniform(8.0, 12.0, 10).round(2),
#     'volume': np.random.randint(100000, 500000, 10)
# })

# # GTBank stock prices - slightly different timestamps
# gtb_times = pd.date_range(start='2023-01-01 09:00:30', 
#                           periods=10, freq='1min')
# gtb = pd.DataFrame({
#     'date_time': gtb_times,
#     'close': np.random.uniform(25.0, 35.0, 10).round(2),
#     'volume': np.random.randint(200000, 600000, 10)
# })

# # Zenith Bank stock prices - slightly different timestamps
# zenith_times = pd.date_range(start='2023-01-01 09:01:00', 
#                              periods=10, freq='1min')
# zenith = pd.DataFrame({
#     'date_time': zenith_times,
#     'close': np.random.uniform(20.0, 28.0, 10).round(2),
#     'volume': np.random.randint(150000, 450000, 10)
# })

# print("Access Bank data:")
# print(access.head())

# print("\nGTBank data:")
# print(gtb.head())

# print("\nZenith Bank data:")
# print(zenith.head())

# # merge_asof() to merge access and gtb
# access_gtb = pd.merge_asof(access, gtb, on='date_time',
#                            suffixes=('', '_gtb'), direction='nearest')

# # merge_asof() to merge access_gtb and zenith
# access_gtb_zenith = pd.merge_asof(access_gtb, zenith, on='date_time',
#                                    suffixes=('_access', '_zenith'), 
#                                    direction='nearest')

# print("\nMerged table:")
# print(access_gtb_zenith.head())

# # Compute price differences
# price_diffs = access_gtb_zenith.diff()

# # Plot price differences
# price_diffs.plot(y=['close_access', 'close_gtb', 'close_zenith'])
# plt.title('Nigerian Bank Stock Price Differences')
# plt.xlabel('Time')
# plt.ylabel('Price Difference (NGN)')
# plt.tight_layout()
# plt.show()

# # Correlation between bank prices
# print("\nPrice correlation between banks:")
# print(access_gtb_zenith[['close_access', 
#                           'close_gtb', 
#                           'close_zenith']].corr())

'''
Using .merge_asof() to create dataset of GDP and recession periods
'''
# # create dates
# dates = pd.date_range(start='2000-01-01', periods=24, freq='QS')

# # Generate GDP dataset - quarterly data
# gdp = pd.DataFrame({
#     'date': dates,
#     'gdp': [
#         10.2, 10.5, 10.8, 11.0, 11.2, 11.5,  # 2000-2001 growth
#         11.3, 10.9, 10.5, 10.2, 10.0, 9.8,   # 2002-2003 recession
#         10.1, 10.5, 10.9, 11.3, 11.8, 12.2,  # 2004-2005 recovery
#         12.5, 12.8, 12.3, 11.8, 11.2, 10.8   # 2006-2007 recession
#     ]
# })

# # Generate recession dataset
# recession = pd.DataFrame({
#     'date': dates,
#     'econ_status': [
#         'normal', 'normal', 'normal', 'normal', 'normal', 'normal',
#         'normal', 'recession', 'recession', 'recession', 'recession', 'recession',
#         'normal', 'normal', 'normal', 'normal', 'normal', 'normal',
#         'normal', 'normal', 'recession', 'recession', 'recession', 'recession'
#     ]
# })

# print("GDP table:")
# print(gdp.head(10))

# print("\nRecession table:")
# print(recession.head(10))

# Merge gdp and recession on date using merge_asof()
# gdp_recession = pd.merge_asof(gdp, recession, on='date', direction='nearest')

# print("\nMerged table:")
# print(gdp_recession)

# Create is_recession list using list comprehension
# is_recession = ['r' if s == 'recession' else 'g' for s in gdp_recession['econ_status']]

# print("\nColor list:")
# print(is_recession)

# # Plot bar chart of gdp vs date colored by recession status
# gdp_recession['date'] = gdp_recession['date'].astype(str)
# gdp_recession.plot( y='gdp', x='date', kind='bar', color=is_recession, rot=90)
# plt.title('GDP vs Recession Periods (2000-2005)')
# plt.xlabel('Date')
# plt.ylabel('GDP (Trillions USD)')
# plt.tight_layout()
# plt.show()

'''
Using .melt() to unpivot a wide table of Nigerian unemployment rates by month
'''
# # Wide format - Nigerian unemployment rate by month
# ur_wide = pd.DataFrame({
#     'year': ['2019', '2020', '2021', '2022'],
#     'Jan': [6.1, 7.2, 8.3, 7.1],
#     'Feb': [6.3, 7.5, 8.1, 6.9],
#     'Mar': [6.5, 7.8, 7.9, 6.7],
#     'Apr': [6.2, 8.1, 7.6, 6.5],
#     'May': [6.0, 8.4, 7.4, 6.3],
#     'Jun': [5.9, 8.6, 7.2, 6.1]
# })

# # Unpivot everything besides the year column
# ur_tall = ur_wide.melt(id_vars='year', var_name='month', value_name='unempl_rate')

# # Create a date column using the month and year columns of ur_tall
# ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])

# # Sort ur_tall by date in ascending order
# ur_sorted = ur_tall.sort_values('date')

# # Plot the unempl_rate by date
# ur_sorted.plot(x='date', y='unempl_rate')
# plt.title('Nigerian Unemployment Rate (2019-2022)')
# plt.xlabel('Date')
# plt.ylabel('Unemployment Rate (%)')
# plt.show()