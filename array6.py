def f1(t):
  return t**2*exp(-t**2)

def f2(t):
  return t**2*f1(t)

t = linspace(0,3,51)

y1 = f1(t)
y2 = f2(t)

plot(t,y1,'r--')
hold = 'on'
plot(t,y2,'bo')
xlabel('t')
title('Plotting two plots in one plot')
show()
