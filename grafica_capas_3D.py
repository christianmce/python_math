import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[2,4,6],[3,8,5],[-1,1,2]])
b = np.array([22,27,2])
sol = np.linalg.solve(A,b)

x,y = np.linspace(0,10,10),np.linspace(0,10,10)
X, Y = np.meshgrid(x, y)

Z1 = 1+X+Y 
Z2 = -50+X+Y
Z3 = 50+X+Y

fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(X, Y, Z1, alpha=0.5,cmap=cm.Accent,rstride=100, cstride=100)
ax.plot_surface(X, Y, Z2, alpha=0.5,cmap=cm.Paired,rstride=100, cstride=100)
ax.plot_surface(X, Y, Z3, alpha=0.5,cmap=cm.Pastel1,rstride=100, cstride=100)

ax.plot((sol[0],),(sol[1],),(sol[2],),lw=2,c='k',marker='o',markersize=7)
ax.set_xlabel('X');ax.set_ylabel('Y');ax.set_zlabel('Z')

plt.show()
