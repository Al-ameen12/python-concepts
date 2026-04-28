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


np.random.seed(42)
random_scores = np.random.randint(0, 100, 10)
print(random_scores)