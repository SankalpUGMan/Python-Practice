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
print len(X)
print len(Y)

ii = numpy.where(X*X + Y*Y <= 0.35*0.35)							#numpy.where stores indices of the matrix
phi[ii] = 1.0


errors = numpy.zeros(1500)

for k in range(Niter):										#we want the error between previous value and the next one
	oldphi = phi.copy()
	phi[1:-1,1:-1] = (0.25)*(phi[1:-1,0:-2] + phi[1:-1,2:] + phi[0:-2,1:-1] + phi[2:,1:-1])
	phi[1:-1,0] = phi[1:-1,1]
	phi[1:-1,24] = phi[1:-1,23]
	phi[0,1:-1] = phi[1,1:-1]
	phi[ii] = 1.0
	errors[k] = numpy.max(abs(phi-oldphi))

print len(phi)
print phi.shape

#surface plot
figure = figure(8)
plotting = axes.Axes3D(figure) 									#Axes3D is the means to do a surface plot
plt.title('The 3-D surface plot of potential')
surf = plotting.plot_surface(Y, X, phi.T, rstride=1, cstride=1, cmap=cm.jet)
plt.show()

#contour plot
plt.figure(9)
contour = plt.contour(a, -b, phi, inline=True)
clabel(contour,inline = 1.0 , fontsize=10)
plt.title('Contour plot of potential')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

#vector plot
Jx=zeros((Ny,Nx))										 #always initialize to zero before playing with matrices 			
Jy=zeros((Ny,Nx))
Jy[1:-1,1:-1]=-0.5*(phi[1:-1,0:-2]-phi[1:-1,2:])
Jx[1:-1,1:-1]=-0.5*(phi[0:-2,1:-1]-phi[2:,1:-1])

plt.figure(10)
plt.plot(a[ii[0]], b[ii[1]], 'ro')
quiver(b, a, Jy[::-1,:], Jx[::-1,:])
plt.title('The vector plot of potential')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

#heat generation
q = Jx**2 + Jy**2 		
plt.figure(11)							         			#the value of sigma is taken to be 1
contour1 = plt.contour(b,-a, q, inline = True)
clabel(contour1,inline = 1,fontsize = 10)
plt.title('The plot of heat generated and temperature variation')
plt.show()
