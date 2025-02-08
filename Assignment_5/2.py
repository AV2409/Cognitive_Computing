import numpy as np

# 2-a
array = np.array([10, 52, 62, 16, 16, 54, 453])
sorted_array = np.sort(array)
sorted_indices = np.argsort(array)
smallest_4 = np.partition(array, 4)[:4]
largest_5 = np.partition(array, -5)[-5:]
print("Sorted array:", sorted_array)
print("Indices of sorted array:", sorted_indices)
print("4 Smallest elements:", smallest_4)
print("5 Largest elements:", largest_5)

# 2-b
array2 = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integers_only = array2[array2 == array2.astype(int)]
floats_only = array2[array2 != array2.astype(int)]
print("Integer elements only:", integers_only)
print("Float elements only:", floats_only)