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
#print X, Y

ii = numpy.where(X*X + Y*Y <= 0.35*0.35)							#numpy.where stores indices of the matrix
phi[ii] = 1.0


errors = numpy.zeros(1500)

for k in range(Niter):										# we want the error between previous value and the next one
	oldphi = phi.copy()
	phi[1:-1,1:-1] = (0.25)*(phi[1:-1,0:-2] + phi[1:-1,2:] + phi[0:-2,1:-1] + phi[2:,1:-1])
	phi[1:-1,0] = phi[1:-1,1]
	phi[1:-1,24] = phi[1:-1,23]
	phi[0,1:-1] = phi[1,1:-1]
	phi[ii] = 1.0
	errors[k] = numpy.max(abs(phi-oldphi))

r = linspace(1,1500,1500)

plt.figure(3)
plt.plot(r, errors, 'ro')
plt.title('Plot of errors plotted as a normal plot')
plt.xlabel('Number of iterations')
plt.ylabel('Errors')
plt.show()

plt.figure(4)
plt.semilogy(r, errors, 'b')
plt.title('Plot of errors plotted as a semilog plot')
plt.xlabel('Number of iterations')
plt.ylabel('Errors')
plt.show()

plt.figure(5)
plt.loglog(r, errors, 'g')
plt.title('Plot of errors plotted as a loglog plot')
plt.xlabel('Number of iterations')
plt.ylabel('Errors')
plt.show()

errors_new1 = numpy.zeros(30)
m = linspace(1,30,30)

for i in range(1,30):
	errors_new1[i] =  errors[50*i]

plt.figure(6)
plt.plot(m, errors_new1, 'ro')
plt.title('Plot of every 50th point plotted in a normal plot')
plt.xlabel('Number of iterations')
plt.ylabel('Errors')
plt.show()
