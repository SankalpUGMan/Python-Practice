import numpy
import matplotlib.pyplot as plt
import math
import scipy.special as spe
from pylab import *
import mpl_toolkits.mplot3d.axes3d as axes

Nx = 25
Ny = 25 
radius = 0.35
Niter = 1500

phi = []
phi = numpy.zeros((Ny,Nx))

a = numpy.linspace(-0.5, 0.5, Nx)
b = numpy.linspace(-0.5, 0.5, Ny)

X,Y = meshgrid(a,b)
print X, Y

ii = numpy.where(X*X + Y*Y <= 0.35*0.35)			#numpy.where stores indices of the matrix
phi[ii] = 1.0

print phi

plt.figure(1)
con=plt.contour(a, b, phi,inline=True)
clabel(con,inline=1,fontsize=10)
plt.title('Contour plot of the region with potential 1 volt')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

plt.figure(2)
plt.plot(a[ii[0]], b[ii[1]], 'ro')
plt.title('The plot of section of wire')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
