import matplotlib.pyplot as plt 
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# initialises figure
plt.figure()

# 2d plot 1
plt.subplot(2, 1, 1)
plt.plot(t1, f(t1), 'bo')
plt.plot(t2, f(t2), 'k')

# plot 2
plt.subplot(2, 1, 2)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()