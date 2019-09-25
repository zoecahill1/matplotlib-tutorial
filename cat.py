import matplotlib.pyplot as plt

#x values
names = ['group_a', 'group_b', 'group_c']
#y values
values = [1, 10, 100]

# change default figure size
# figsize=(width and height)
plt.figure(figsize=(9, 3))

plt.subplot(1, 3, 1)
# draw a bar plot
plt.bar(names, values)

plt.subplot(132)
plt.scatter(names, values)

plt.subplot(1, 3, 3)
# linewidth alters the width of the line
plt.plot(names, values, linewidth=2.0)

# Overall title
plt.suptitle('Categorical Plotting')
plt.show()