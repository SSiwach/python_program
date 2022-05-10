def H_loop(x):
  r = np.zeros(len(x))
  for i in arange(len(x)):
    r[i] = H(x[i])
  return r

x = np.linspace(-5,5,6)
y = H_loop(x)

plt.plot(x,y)
