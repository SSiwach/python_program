from numpy import *
from matplotlib.pyplot import *

def f(t):
  return t**2*exp(-t**2)

t = linspace(0,3,51)
y = zeros(len(t))
for i in arange(len(t)):
  y[i] = f(t[i])
legend(['t^2*exp(-t^2)'])
axis([0,3,-0.05,0.6])
title('My first plot')
plot(t,y)
show()

savefig('tmp1.pdf')
savefig('timp1.png')
