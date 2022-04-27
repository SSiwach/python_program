x = np.ones((3, 5, 5), dtype=np.int16)
print(x)
y = np.ones((1,5,5))

x = np.full((3, 3, 3), dtype=np.int16, fill_value = 5)
print(x)

x = np.tri(5,5,k = 0,dtype = np.uint16)
print(x)

x = np.ones((5, 5), dtype=np.uint8)
y = np.triu(x, k=0)
print(y)

x = np.ones((5, 5), dtype=np.uint8)
y = np.triu(x, k=-1)
print(y)

x = np.arange(6)
import matplotlib.pyplot as plt

print(x)
type(x)

y = x +1 
plt.plot(x,y,'o-')
plt.plot(x,-y,'o--')
plt.title('y = x and y = -x')
plt.show()

N = 30
x =np.linspace(0,15,N)
#print(x)

y = x
plt.plot(x,y,'o--')

plt.axis('off')

plt.show()

N = 30
y = np.logspace(0.1,2,N)

plt.plot(x,y,'o--')

plt.show()
