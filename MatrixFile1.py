import numpy as np
import matplotlib.pyplot as plt 
from statistics import mean

#make random data x and half the data y
x = np.random.normal(0.0, 1, 240)
y = 0.5*np.random.normal(0.0, 1, 240)

x2 = np.random.normal(0.0, 1, 240) + 1
y2 = 0.2*np.random.normal(0.0, 1, 240) - 1.5 

plt.scatter(x, y, label = 'data1', facecolors = 'none', edgecolors = 'b')
plt.legend()
plt.scatter(x2,y2, label = 'data2', facecolors = 'none', edgecolors = 'r')
plt.legend()
plt.title('random data test')
plt.show()

