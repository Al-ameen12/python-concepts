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
palette_colors = {'Rural': "green", 'Urban': "blue"}

# Create a count plot of school with location subgroups
sns.countplot(data = student_data, x = 'school', hue = 'location', palette = palette_colors )
# Show plot
plt.show()