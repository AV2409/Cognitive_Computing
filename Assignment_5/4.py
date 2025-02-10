import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot(x, x**2)
plt.title("Y = x^2")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, np.sin(x))
plt.title("Y = sin(x)")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, np.exp(x))
plt.title("Y = e^x")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, np.log(np.abs(x) + 1))
plt.title("Y = log(|x| + 1)")
plt.grid(True)

plt.tight_layout()
plt.show()