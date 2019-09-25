import matplotlib.pyplot as plt
import numpy as np 

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        # rand use for random floats
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
# absolute gets rid of negatives
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.title("Exmaple of 4D data plotting")
plt.xlabel('entry A')
plt.ylabel('entry B')

plt.show()