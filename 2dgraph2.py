import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(0.0, 5.0, 0.2)

plt.plot(x, x, "r--", label="Line 1")
plt.plot( x, x**2, "g^", label="Line 2") 
plt.plot(x, x**3, "bo", label="Line 3")

plt.title("A graph with 3 plots")
plt.xlabel("X Values")
plt.ylabel("Y values")

plt.legend()
plt.show()