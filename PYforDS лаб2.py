import numpy as np

#1
arr = np.random.randint(-100, 101, 200)
print("task 1:\n", arr)
#2
posnums_mask = arr > 0
posnums_numbers = arr[posnums_mask]
print("task 2:\n", posnums_numbers)

#3
arr[arr < 0] = 0
print("task 3:\n", arr)

#4
mean_value = arr.mean()
print("task 4:\n", mean_value)

