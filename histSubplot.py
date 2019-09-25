import matplotlib.pyplot as plt 
import numpy as np 

# .subplot(row, column, graph number 1)
plt.subplot(1, 2, 1)
# normal will show us numbers distributed around a bellcurve
# .normal(center, strect out, amt of nums we want)
x = np.random.normal(0.0, 1.0, 10000)
plt.hist(x, bins=35, ec="black")
plt.title("Normal Distribution")
plt.axis([-3, 3, 0, 1000])
plt.grid(True)

plt.subplot(1, 2, 2)
# uniform will give us a range of nums(between -3.0 and 3.0)
# distributed evenly across range
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x, bins=35, ec="black")
plt.title("Uniform Distribution")
plt.axis([-3, 3, 0, 1000])
plt.grid(True)

plt.show()