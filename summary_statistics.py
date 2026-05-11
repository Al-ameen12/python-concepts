
import pandas as pd

# Read the sales data into a DataFrame
sales = pd.read_csv("sales_subset.csv", index_col=0)
sales_1_1 = sales.copy()


# # Print the head of the sales DataFrame
# print(sales.head())

# # Print the info about the sales DataFrame
# print(sales.info())

# # Print the mean of weekly_sales
# print(sales["weekly_sales"].mean())

# # Print the median of weekly_sales
# print(sales['weekly_sales'].median())


# print(sales.shape)


# Print the maximum of the date column
# print(sales['date'].max())

# # Print the minimum of the date column
# print(sales['date'].min())


# TASK
# Use the custom iqr function defined for you along with .agg() 
# to print the IQR of the temperature_c column of sales.

# A custom IQR function
# def iqr(column):
#     return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
# print(sales['temperature_c'].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
# print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
# print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, "median"]))


##### Cumulative statistics #######

# # Sort sales_1_1 by date
# sales_1_1 = sales_1_1.sort_values('date')


# # Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
# sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# # Get the cumulative max of weekly_sales, add as cum_max_sales col
# sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# # See the columns you calculated
# print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])


# # Drop duplicate store/type combinations
# store_types = sales.drop_duplicates(subset=['store', 'type'])
# print(store_types.head())

# # Drop duplicate store/department combinations
# store_depts = sales.drop_duplicates(subset=['store', 'department'])
# print(store_depts.head())

# # Subset the rows where is_holiday is True and drop duplicate dates
# holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates(subset='date')

# # Print date col of holiday_dates
# print(holiday_dates['date'])
