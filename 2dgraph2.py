import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(0.0, 5.0, 0.2)

plt.plot(x, x, "r--", x, x**2, "g^", x, x**3, "bo")

plt.show()