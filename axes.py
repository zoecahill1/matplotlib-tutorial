import matplotlib.pyplot as plt

# the first figure
plt.figure(1)


# the first subplot in the first figure
plt.subplot(2, 1, 1)
plt.plot([1, 2, 3])

# the second subplot in the first figure
plt.subplot(2, 1, 2)
plt.plot([4, 5, 6])

# a second figure
plt.figure(2)
# creates a subplot(111) by default
plt.plot([4, 5, 6])


#figure 1 current; subplot(212) still current
plt.figure(1)
# make subplot(211) in figure1 current
plt.subplot(2, 1, 1) 
 # subplot 211 title
plt.title('Easy as 1, 2, 3')

plt.show()
# call close() if making multiple figures!