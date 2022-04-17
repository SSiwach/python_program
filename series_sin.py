from sympy import exp, sin, cos
f = exp(t)
f.series(t, 0, 3)

f = exp(sin(t))
f.series(t, 0, 8)
