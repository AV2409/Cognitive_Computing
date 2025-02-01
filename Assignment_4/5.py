import numpy as np

ucs420_akshansh = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])

mean_val = np.mean(ucs420_akshansh)
median_val = np.median(ucs420_akshansh)
max_val = np.max(ucs420_akshansh)
min_val = np.min(ucs420_akshansh)
unique_vals = np.unique(ucs420_akshansh)

reshaped_ucs420_akshansh = ucs420_akshansh.reshape(4, 3)
resized_ucs420_akshansh = ucs420_akshansh[:2, :3]

print("Mean:", mean_val)
print("Median:", median_val)
print("Max:", max_val)
print("Min:", min_val)
print("Unique Elements:", unique_vals)
print("Original:\n",ucs420_akshansh)
print("Reshaped (4x3):\n", reshaped_ucs420_akshansh)
print("Resized (2x3):\n", resized_ucs420_akshansh)