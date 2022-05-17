fig = plt.figure(3)
ax = fig.gca()
ax.contour(xv,yv,hv)
plt.axis('equal')

fig = plt.figure(4)
ax = fig.gca(projection='3d')
ax.contour(xv,yv,hv)

fig = plt.figure(5)
ax = fig.gca(projection='3d')
ax.plot_surface(xv,yv,hv,cmap = cm.coolwarm, rstride = 1, cstride = 1)

ax.contour(xv,yv,hv,zdir = 'z', offset =-1000, cmap = cm.coolwarm)
ax.contour(xv,yv,hv,zdir = 'x', offset = -10, cmap = cm.coolwarm)
ax.contour(xv,yv,hv,zdir = 'y', offset = 10, cmap= cm.coolwarm)

fig = plt.figure(6)
ax = fig.gca()
ax.imshow(hv)

fig = plt.figure(7)
ax = fig.gca()
ax.contour(xv,yv,hv,10)

fig = plt.figure(8)
ax = fig.gca()
ax.contour(xv,yv,hv,10,colors = 'k')
plt.axis('equal                  b')
