import matplotlib.pyplot as plt
import numpy as np

# plot between -2 and 2
x = np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1)

plt.plot(x, np.sin(x), 'g.', label="sin")
plt.plot(x, np.cos(x), 'b.', label="cos")

plt.title("Plotting sin vs cos")
plt.legend()

plt.show()