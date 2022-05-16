import numpy as np
import matplotlib.pyplot as plt
h0 = 2.27
R = 4
x2 = y2 = np.linspace(-10,10,110)
x2v, y2v = np.meshgrid(x2,y2,indexing ='ij',sparse = False)
h2v = h0/(1 + (x2v**2 + y2v**2)/(R**2))
dhdx, dhdy = np.gradient(h2v)
plt.plot(x2,dhdx)
