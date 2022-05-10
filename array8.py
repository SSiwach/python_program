def f1(t):
  return t**2*np.exp(-t**2)
def f2(t):
  return t**2*f1(t)

t = np.linspace(0,3,51)

y1 = f1(t)

y2 = f2(t)

plt.plot(t,y1,'r-')
plt.plot(t,y2,'bo')
plt.xlabel('t')
plt.ylabel('y')
plt.legend('t^2*exp(-t^-2)','t^4*exp(-t^2)')

plt.title('Plotting two curves in the same plot')

plt.savefig('tmp3.pdf')

plt.show
