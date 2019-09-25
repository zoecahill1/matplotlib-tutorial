import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.normal(0.0, 1.0, 1000)

# bins is number of ranges for plot, alpha is transparency (default is 1)
# color is green, ec is for edge colour,
plt.hist(x, bins=30, color="g", ec="black", alpha=0.75)

plt.title("A simple histogram")
plt.xlabel("Distribution")
plt.ylabel("Number of occurances")

# setting axis ticks [xmin, xmax, ymin, ymax]
plt.axis([-3, 3, 0, 100])

# plt.text(x,y, "string") https://matplotlib.org/3.1.1/tutorials/text/text_intro.html
plt.text(-2.5, 90, "Text on graph")

# adds grid to background
plt.grid(True)

plt.show()

