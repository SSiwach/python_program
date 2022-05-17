import matplotlib.pyplot as plt
import numpy as np

h0 = 2.772
R = 4

fig = plt.figure(3)
x = y = np.linspace(-10., 10., 41)
xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)
hv = h0/(1 + (xv**2+yv**2)/(R**2))
ax = fig.gca()
ax.contour(xv,yv,hv)
plt.axis('equal')
