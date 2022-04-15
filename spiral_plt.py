import numpy as np
import nnfs

from nnfs.datasets import spiral_data
nnfs.init() # set seed = 0; creates a float32 type default; overrides the original dot product from NumPy

import matplotlib.pyplot as plt

X, y = spiral_data(samples = 100, classes = 3)

plt.scatter(X[:,0],X[:,1], c=y, cmap = 'brg')

plt.show()

