fig = plt.figure(1)
ax = fig.gca(projection = '3d')
ax.plot_wireframe(xv,yv,hv,rstride = 2, cstride = 2)

fig= plt.figure(2)
ax = fig.gca(projection = '3d')
from matplotlib import cm
ax.plot_surface(xv,yv,hv,cmap=cm.coolwarm, rstride = 1, cstride = 1)

ax.plot(curve_x,curve_y,curve_z,linewidth = 5)
