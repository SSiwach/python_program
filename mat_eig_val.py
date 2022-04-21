from numpy import *
from numpy.linalg import *

A = array([ [1,2,3],[22,32,42],[55,66,100] ])

print('A = ', A)

b = array([1,2,3])

print('b = ', b)

from numpy.linalg import solve

x = solve(A,b)

print('x = ',x)

print('Residual = ',dot(A,x) - b)
