import numpy as np
import math
N = 10
x = np.zeros(N)
y = np.zeros(N)

dx = 2.0/(N-1)
for i in range(N):
  x[i] = -1 + dx*i
  y[i] = math.exp(-x[i]*x[i])
  plt.plot(x[i],y[i])
