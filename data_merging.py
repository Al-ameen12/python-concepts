import pandas as pd

taxi_owners = pd.read_csv('taxi_owners.csv')
taxi_veh = pd.read_csv('taxi_vehicles.csv')


wards = pd.read_csv('Chicago_wards.csv')
census = pd.read_csv('Chicago_census.csv')

wards_altered = wards.copy()
census_altered = census.copy()


licenses = pd.read_csv('licenses.csv')
biz_owners = pd.read_csv('business_owners.csv')


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
licenses_owners = licenses.merge(biz_owners, on = 'account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})
# an alternative way to do the above is: 
# counted_df = licenses_owners.groupby('title')['account'].count()

# Sort the counted_df in descending order
sorted_df = counted_df.sort_values('account', ascending = False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())