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

def exp(t):
	m = numpy.exp(t)
	return m

def double_cosine(t):
	n = numpy.cos(numpy.cos(t))
	return n

x = linspace(0, 2*(math.pi), 401)
x = x[:-1]
n = numpy.arange(0, 26)

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

c_exp_a = []
c_exp_b = []

value1 = c_exp[0]
c_exp_a.append(value1)
c_exp_b.append(0)

for i in range(1,26):
	c_exp_a.append(c_exp[2*i-1])
	c_exp_b.append(c_exp[2*i]) 

c_double_cosine_a = []
c_double_cosine_b = []

value2 = c_double_cosine[0]
c_double_cosine_a.append(value2)
c_double_cosine_b.append(0)

for i in range(1,26):
	c_double_cosine_a.append(c_double_cosine[2*i-1])
	c_double_cosine_b.append(c_double_cosine[2*i]) 

exp_mult = numpy.matmul(A, c_exp)
double_cosine_mult = numpy. matmul(A, c_double_cosine)

plt.figure(1)
plt.plot(x, exp_mult, 'bo')
plt.plot(x, b_exp, 'ro')
plt.xlabel('x')
plt.ylabel('$e^x$')
plt.title('Plot of exponential plots calculated using two different methods')
plt.grid(True)

plt.figure(2)
plt.plot(x, double_cosine_mult, 'bo')
plt.plot(x, b_double_cosine, 'ro')
plt.xlabel('x')
plt.ylabel('$cos(cos(x))$')
plt.title('Plot of double cosine plots calculated using two different methods')
plt.grid(True)
plt.show()
