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

p = [math.log(x) for x in errors]
C = numpy.zeros((Niter, 2))

for i in range(Niter):
	C[i,0] = 1
	C[i,1] = i

M = lstsq(C, p, rcond = -1)[0]
e = M[0]
f = M[1]
A = numpy.exp(e)
B = f

print A, B

error_new1 = numpy.matmul(C, M)
s = numpy.exp(error_new1)

q = p[500:1500]
D = numpy.zeros((1000, 2))

for i in range(1, 1000):
	D[i,0] = 1
	D[i,1] = i + 500

N = lstsq(D, q, rcond = -1)[0]
g = N[0]
h = N[1]
A_new = numpy.exp(g)
B_new = h
error_new2 = numpy.matmul(D, N)
t = numpy.exp(error_new2)

r = linspace(1,1500,1500)
n = linspace(500,1500,1000)

plt.figure(7)
plt.semilogy(r, errors, 'r', label = 'errors')
plt.semilogy(r, s, 'b', label = 'fit1')
plt.semilogy(n, t, 'g', label = 'fit2')
plt.title('Plot of errors ,fit1 and fit2')
plt.xlabel('Number of iterations')
plt.ylabel('Errors')
plt.legend()
plt.show()

N
Error = abs((-A/B)*(numpy.exp(B*( + 0.5))))
print Error
