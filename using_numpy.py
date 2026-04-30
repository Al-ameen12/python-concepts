import numpy as np

# heights = [1.75, 1.80, 1.65, 1.90]
           
# np_heights = np.array(heights)

# print(np_heights)
# print(type(np_heights))


# heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
# weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

# bmi = weights / heights ** 2

# print(bmi)

# heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
# print(np.mean(heights))
# print(np.median(heights))
# print(np.std(heights))
# print(np.max(heights))
# print(np.min(heights))


# scores = np.array([45, 78, 62, 91, 55, 83])

# print(np.mean(scores))
# print(np.max(scores), np.min(scores))
# print(scores[scores > 60])



# data = np.array([[45, 78, 62],
#                  [91, 55, 83],
#                  [72, 66, 88]])

# print(data.shape)        # dimensions of the array
# print(data[:, 0])        # entire first column
# print(data[1, :])        # entire second row
# print(np.mean(data, axis=0))  # average of each column


# np.random.seed(42)
# random_scores = np.random.randint(0, 100, 10)
# print(random_scores)


# comparing Arrays
# They both contain the areas for the kitchen, living room, bedroom and bathroom in the same order, so you can compare them.
# Create arrays
# import numpy as np
# my_house = np.array([18.0, 20.0, 10.75, 9.50])
# your_house = np.array([14.0, 24.0, 14.25, 9.0])

# # my_house greater than or equal to 18
# print(my_house >= 18)

# # my_house less than your_house
# print(my_house < your_house)


'''
Boolean operators with NumPy

Before, the operational operators like < and >= worked with NumPy arrays out of the box. 
Unfortunately, this is not true for the boolean operators and, or, and not.

To use these operators with NumPy, you will need np.logical_and(), np.logical_or() and np.logical_not(). 
Here's an example on the my_house and your_house arrays from before to give you an idea:

np.logical_and(my_house > 13, 
               your_house < 15)
'''
# Create arrays

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11, your_house<11))