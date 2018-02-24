 # coding: utf-8

from scipy.integrate import quad
from pylab import *
from matplotlib import pyplot as plt
import numpy
from scipy import *

def exp(t):
	m = numpy.exp(t)
	return m

def double_cosine(t):
	n = numpy.cos(numpy.cos(t))
	return n


x = linspace(0, 2*(math.pi), 401)
x = x[:-1]

b_exp = exp(x)							#order of defining a function is important
b_double_cosine = double_cosine(x)
 								# drop last term to have a proper periodic integral
A = zeros((400,51))						# allocate space for A
A[:,0] = 1							# col 1 is all ones

for k in range(1,26):
	A[:,2*k-1] = cos(k*x) 					# cos(kx) column
	A[:,2*k] = sin(k*x)					# sin(kx) column
			
c_exp = lstsq(A,b_exp)[0]					# the ’[0]’ is to pull out the best fit vector. lstsq returns a list.
c_double_cosine = lstsq(A,b_double_cosine)[0]

print(c_exp)
print(c_double_cosine)

n = numpy.arange(0, 26)
print(n)

c_exp_a = []
c_exp_b = []

value1 = c_exp[0]
c_exp_a.append(value1)
c_exp_b.append(0)

for i in range(1,26):
	c_exp_a.append(c_exp[2*i-1])
	c_exp_b.append(c_exp[2*i]) 

print(c_exp_a)
print(c_exp_b)

c_exp_a = list(map(abs,c_exp_a))
c_exp_b = list(map(abs,c_exp_b))
	
plt.figure(7)
plt.loglog(n, c_exp_a, 'bo')
plt.loglog(n, c_exp_b, 'go')
plt.xlabel('n')
plt.ylabel('Matrix Calculated Exponential fourier points')
plt.title('Plot of loglog matrix calculated exponential function fourier points')
plt.grid(True)

plt.figure(8)
plt.semilogy(n, c_exp_a, 'bo')
plt.semilogy(n, c_exp_b, 'go')
plt.xlabel('n')
plt.ylabel('Matrix Calculated Exponential fourier points')
plt.title('Plot of semilog matrix calculated exponential function fourier points')
plt.grid(True)

c_double_cosine_a = []
c_double_cosine_b = []

value2 = c_double_cosine[0]
c_double_cosine_a.append(value2)
c_double_cosine_b.append(0)

for i in range(1,26):
	c_double_cosine_a.append(c_double_cosine[2*i-1])
	c_double_cosine_b.append(c_double_cosine[2*i]) 

print(c_double_cosine_a)
print(c_double_cosine_b)

c_double_cosine_a = list(map(abs,c_double_cosine_a))
c_double_cosine_b = list(map(abs,c_double_cosine_b))
	
plt.figure(9)
plt.loglog(n, c_double_cosine_a, 'bo')
plt.loglog(n, c_double_cosine_b, 'go')
plt.xlabel('n')
plt.ylabel('Matrix Calculated Double Cosine fourier points')
plt.title('Plot of loglog matrix calculated double cosine function fourier points')
plt.grid(True)

plt.figure(10)
plt.semilogy(n, c_double_cosine_a, 'bo')
plt.semilogy(n, c_double_cosine_b, 'go')
plt.xlabel('n')
plt.ylabel('Matrix Calculated Exponential fourier points')
plt.title('Plot of semilog matrix calculated double cosine function fourier points')
plt.grid(True)
plt.show()
