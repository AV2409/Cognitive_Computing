import numpy as np

arr = np.array([1, 2, 3, 6, 4, 5])
print("Original Array:", arr)

# 2-a
arr_rev = arr[::-1]
print("Reversed Array:", arr_rev)

# 2-b
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

unique_x, counts_x = np.unique(x, return_counts=True)
max_count_index_x = np.argmax(counts_x)
most_freq_x = unique_x[max_count_index_x]
indices_x = np.where(x == most_freq_x)[0]

unique_y, counts_y = np.unique(y, return_counts=True)
max_count_index_y = np.argmax(counts_y)
most_freq_y = unique_y[max_count_index_y]
indices_y = np.where(y == most_freq_y)[0]

print("Most Frequent in x:", most_freq_x, "at indices", indices_x)
print("Most Frequent in y:", most_freq_y, "at indices", indices_y)

