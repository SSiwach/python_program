import matplotlib.pyplot as plt

def f(x):
  return x**3
n = 5
dx = 1.0/(n-1)
xlist = [i*dx for i in range(n)]
ylist = [f(x) for x in xlist]
pairs = [[x,y] for x, y in zip(xlist, ylist)]
pairs
plt.plot(x,y)
