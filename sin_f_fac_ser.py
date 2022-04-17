x = 1.2 # assign some value
N = 100 # number of iteration # maximum power in sum
k = 1 #K initilization
s = x # first term in teh sin(x) expansion
sign = 1.0 #sign of the first term
import math
while k < N:
  sign = - sign
  k = k + 2
  term = sign*x**k/math.factorial(k)
  s = s + term
print('sin(%g) = %g (approximation with %d terms)' % (x, s, N))
