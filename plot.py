import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 1.0, 10)
y = np.random.normal(0.0, 1.0, 10)

line, = plt.plot(x, y, '-')
# makes thicker
line.set_antialiased(False)

plt.show()