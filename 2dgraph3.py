import matplotlib.pyplot as plt 
import numpy as np 

# same as range(start, stop, step)
x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0
# generate normally distributed random data (like bell curve)
# np.random.noraml(mean(ie middle of bell curve), standard deviation(set to 1 as default), size or shape of data)
noise = np.random.normal(0.0, 1.0, len(x)) # https://www.sharpsightlabs.com/blog/numpy-random-normal/

plt.plot(x, y + noise, "r.")
plt.plot(x, y, "b-")

plt.show()

