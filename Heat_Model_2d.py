import numpy as np
import time
import scipy
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


size = 20 #size of the 2D grid

#Equation Parameters
dt = 0.1
dx = 0.1
alpha = 0.01

#Laplacian numerical calculation function
def lap(Z):
	#special Y matrix
	Y = Z #Overwrappign 
	Y[0, :] = Z[-2, :]
	Y[-1, :] = Z[1, :]
	Y[:, 0] = Z[:, -2]
	Y[:, -1] = Z[:, 1]
    # Ztop = Z[0:-2,1:-1]
    # Zleft = Z[1:-1,0:-2]
    # Zbottom = Z[2:,1:-1]
    # Zright = Z[1:-1,2:]
    # Zcenter = Z[1:-1,1:-1]
	Ztop = Y[:-2,1:-1]
	Zleft = Y[1:-1,:-2]
	Zbottom = Y[2:,1:-1]
	Zright = Y[1:-1,2:]
	Zcenter = Y[1:-1,1:-1]
	return (Ztop + Zleft + Zbottom + Zright - 4 * Zcenter) / dx**2


#Initializing Vectors
T = np.zeros((size, size))
#T[1: -1, 1: -1] = np.random.random((size-2, size-2))
#Figure
fig = plt.figure(figsize = (15, 10))
ax = fig.gca(projection='3d')

X = np.linspace(-1, 1, size)
Y = np.linspace(-1, 1, size)
X, Y = np.meshgrid(X, Y)
T[1: -1, 1: -1] = 3*np.exp(-(X[1: -1, 1: -1]**2/0.1+Y[1: -1, 1: -1]**2/0.1))
def update(*args):
        
	T[1:-1, 1:-1] += dt*(alpha*lap(T))
	ax.clear()
	plot = ax.plot_surface(X, Y, T, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False, vmin=0., vmax=2.)
	ax.set_zlim(0., 1.5)
        
	#fig.colorbar(plot, shrink=0.5, aspect=5)
	return plot,

ani = animation.FuncAnimation(fig, update, interval=0.1, blit=False)
pl.show()
