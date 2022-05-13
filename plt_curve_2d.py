import matplotlib.pyplot as plt

x= y= np.linspace(-10,10,41)
xv,yv = np.meshgrid(x,y,indexing='ij',sparse = False)
h0 = 2.277
R = 4
hv = h0/(1+(xv**2+yv**2)/(R**2))

plt.plot(x,hv)
