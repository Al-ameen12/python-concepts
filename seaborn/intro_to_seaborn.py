# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



# # Create a DataFrame from csv file
# df = pd.read_csv('seaborn/datasets/young-people-survey-responses.csv', index_col=0)

# # Create a count plot with "Spiders" on the x-axis
# sns.countplot(data = df, x= 'Spiders')

# # Display the plot
# plt.show()
# print(df.head())
# print(df.columns)


student_data = pd.read_csv('seaborn/datasets/student-alcohol-consumption.csv')
mpg = pd.read_csv('seaborn/datasets/mpg.csv')

'''
What is Seaborn first:
Seaborn is built on top of Matplotlib — it produces more beautiful charts with less code. 
Think of Matplotlib as the engine and Seaborn as the better looking car body on top of it.

countplot:
Counts how many times each category appears in a column and displays it as bars.


'''

# data = pd.DataFrame({
#     'city': ['Lagos', 'Abuja', 'Lagos', 'Kano', 
#              'Lagos', 'Abuja', 'Kano', 'Lagos']
# })

# countplot — counting categories:
# sns.countplot(data=data, x='city')


# plt.show()




# Create a scatter plot of absences vs. final grade
# sns.scatterplot(data = student_data, x = 'absences', y = 'G3',hue = 'location' )

# Change the legend order in the scatter plot
# sns.scatterplot(x="absences", y="G3", 
#                 data=student_data, 
#                 hue="location", 
#                 hue_order = ['Rural', 'Urban'])

# Create a dictionary mapping subgroup values to colors
# palette_colors = {'Rural': "green", 'Urban': "blue"}

# # Create a count plot of school with location subgroups
# sns.countplot(data = student_data, x = 'school', hue = 'location', palette = palette_colors )
# # Show plot
# plt.show()


'''
Use relplot() to create a scatter plot of absences vs. final grade, 
with study_time as the row facet.
'''
# Change to use relplot() instead of scatterplot()
# sns.relplot(x="absences", y="G3", 
#             data=student_data,
#             kind="scatter", 
#             row ="study_time",)


#  Adjust further to add subplots based on family support
# sns.relplot(x="G1", y="G3", 
#             data=student_data,
#             kind="scatter",
#             col = 'schoolsup', #subplot based on school support
#             col_order = ['yes', 'no'],
#             row="famsup",      #subplot based on family support
#             row_order=["yes", "no"])



# Create scatter plot of horsepower vs. mpg
# sns.relplot(x="horsepower", y="mpg", 
#             data=mpg, kind="scatter",
#             hue = 'cylinders', 
#             size="cylinders")



# Create a scatter plot of acceleration vs. mpg
# sns.relplot(data = mpg, kind = 'scatter', 
#             x = 'acceleration', y = 'mpg', 
#             hue = 'origin', style = 'origin')


'''
Line plots are used to visualize the relationship between two variables,
Line plots are particularly useful for showing trends over time or continuous data.

confidence intervals are shaded areas around the line that represent the uncertainty of the estimate.
standard deviation (sd) is a measure of the amount of variation or dispersion in a set of values.
'''
# Create line plot

# sns.relplot(x = 'model_year', y = 'mpg', data = mpg, kind = 'line')


# Make the shaded area show the standard deviation
# sns.relplot(x="model_year", y="mpg",
#             data=mpg, kind="line", errorbar='sd') #without a ci


# Create line plot of model year vs. horsepower
# sns.relplot(data = mpg, x = 'model_year', 
#             y = 'horsepower', kind = 'line', 
#             errorbar = None)


# Change to create subgroups for country of origin,  
# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line",
            errorbar=None, style="origin",
            hue="origin", markers = True,
            dashes = False)
# Show plot
plt.show()