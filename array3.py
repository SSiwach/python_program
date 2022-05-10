from math import sin, cos, exp
import numpy as np
x = np.linspace(0,1,201101)
r = np.zeros(len(x))
for i in np.arange(len(x)):
  r[i] = sin(np.pi*x[i])*cos(x[i])*exp(-x[i]**2)+2+x[i]**2

plt.plot(x,r)
