import numpy as np

def f(x):
  return np.sin(1.0/x)

x1 = linspace(-1,1,10)
x2 = linspace(-1,1,1000)

plot(x1,f(x1),label = '%d points' %len(x))
plot(x2,f(x2),label = '%d points' %len(x))
