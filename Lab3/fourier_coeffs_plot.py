from scipy.integrate import quad
from pylab import *
from matplotlib import pyplot as plt
import numpy

def exp_cosine(x,k):
	m = numpy.exp(x)
	u = m*cos(k*x)
	return u

def exp_sine(x,k):
	m = numpy.exp(x)
	u = m*sin(k*x)
	return u
	
def double_cosine_cosine(x,k):
	n = numpy.cos(numpy.cos(x))
	v = n*cos(k*x)
	return v

def double_cosine_sine(x,k):
	n = numpy.cos(cos(x))
	v = n*sin(k*x)
	return v

n = numpy.arange(0,26)

a = []
b = []
value1 = (1/(2*math.pi))*quad(exp_cosine, 0, 2*(math.pi), args = (0))[0] 
a.append(value1)
b.append(0)

for i in range(1,26):								
	a.append((1/(math.pi))*quad(exp_cosine, 0, 2*(math.pi), args=(i))[0])

for j in range(1,26):
	b.append((1/(math.pi))*quad(exp_sine, 0, 2*(math.pi), args=(j))[0])

a = list(map(abs,a))
b = list(map(abs,b))

plt.figure(3)
plt.loglog(n, a, 'ro')
plt.loglog(n, b, 'bo')
plt.xlabel('n')
plt.ylabel('Exponential fourier points')
plt.title('Plot of loglog exponential function fourier points')
plt.grid(True)
plt.legend()

plt.figure(4)
plt.semilogy(n, a, 'ro')
plt.semilogy(n, b, 'bo')
plt.xlabel('n')
plt.ylabel('Exponential fourier points')
plt.title('Plot of semilog exponential function fourier points')
plt.grid(True)
plt.legend()

A = []
B = []

value2 = (1/(2*math.pi))*quad(double_cosine_cosine, 0, 2*(math.pi), args = (0))[0] 
A.append(value2)
B.append(0)

for k in range(1,26):
	A.append((1/(math.pi))*quad(double_cosine_cosine, 0, 2*(math.pi), args = (k))[0])

for l in range(1,26):
	B.append((1/(math.pi))*quad(double_cosine_sine, 0, 2*(math.pi), args = (l))[0])

A = list(map(abs,A))
B = list(map(abs,B))
	
plt.figure(5)
plt.loglog(n, A, 'ro')
plt.loglog(n, B, 'bo')
plt.xlabel('n')
plt.ylabel('Double Cosine fourier points')
plt.title('Plot of loglog double cosine function fourier points')
plt.grid(True)
plt.legend()

plt.figure(6)
plt.semilogy(n, A, 'ro')
plt.semilogy(n, B, 'bo')
plt.xlabel('n')
plt.ylabel('Double Cosine fourier points')
plt.title('Plot of semilog double cosine function fourier points')
plt.grid(True)
plt.legend()
plt.show()
