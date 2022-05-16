from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(1)
ax = fig.gca(projection='3d')

#2d Scaler field plot ax.plot_wireframe = wire frame plot
#2d ax.plot_surface = color the surface
x = y = np.linspace(-10., 10., 41)
xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)
hv = h0/(1 + (xv**2+yv**2)/(R**2))

fig = plt.figure(1)
ax = fig.gca(projection = '3d')
ax.plot_wireframe(xv,yv,hv,rstride = 1 , cstride = 4)

