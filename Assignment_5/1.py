import numpy as np

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
print("Original Matrix:\n",gfg)
print("Sum of all elements:", np.sum(gfg))
print("Sum of all elements row-wise:\n", np.sum(gfg, axis=1))
print("Sum of all elements column-wise:", np.sum(gfg, axis=0))