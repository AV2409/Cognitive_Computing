import numpy as np

akshansh = np.linspace(10, 100, 25)
print("Array:", akshansh)

print("Dimensions:", akshansh.ndim)
print("Shape:", akshansh.shape)
print("Total Elements:", akshansh.size)
print("Data Type:", akshansh.dtype)
print("Total Bytes:", akshansh.nbytes)

reshaped = akshansh.reshape(25, 1)
print("Transpose using reshape:\n", reshaped)

print("Transpose using T attribute:\n", reshaped.T)