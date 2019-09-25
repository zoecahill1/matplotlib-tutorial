# Adapted from https://matplotlib.org/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt 

# plt.plot(x, y, style) style list -> https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "bo")
# The axis() command takes a list of [xmin, xmax, ymin, ymax] to show viewpoint of axis
plt.axis([0, 6, 0, 20])
plt.ylabel("Y values")
plt.xlabel("X values")

plt.show()
