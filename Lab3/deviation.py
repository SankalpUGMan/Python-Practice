 # coding: utf-8

from scipy.integrate import quad
from pylab import *
from matplotlib import pyplot as plt
import numpy
from scipy import *

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

def exp(t):
	m = numpy.exp(t)
	return m

def double_cosine(t):
	n = numpy.cos(numpy.cos(t))
	return n

#Start of quad computed points

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

A = []
B = []
value2 = (1/(2*math.pi))*quad(double_cosine_cosine, 0, 2*(math.pi), args = (0))[0] 
A.append(value2)
B.append(0)

for k in range(1,26):
	A.append((1/(math.pi))*quad(double_cosine_cosine, 0, 2*(math.pi), args = (k))[0])

for l in range(1,26):
	B.append((1/(math.pi))*quad(double_cosine_sine, 0, 2*(math.pi), args = (l))[0])

# Start of matrix calculated points

x = linspace(0, 2*(math.pi), 401)
x = x[:-1]

b_exp = exp(x)							#order of defining a function is important
b_double_cosine = double_cosine(x)
 								# drop last term to have a proper periodic integral
M = zeros((400,51))						# allocate space for M
M[:,0] = 1							# col 1 is all ones

for k in range(1,26):
	M[:,2*k-1] = cos(k*x) 					# cos(kx) column
	M[:,2*k] = sin(k*x)					# sin(kx) column
			
c_exp = lstsq(M,b_exp)[0]					# the ’[0]’ is to pull out the best fit vector. lstsq returns a list.
c_double_cosine = lstsq(M,b_double_cosine)[0]

n = numpy.arange(0, 26)

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

# Deviation program

print('a-terms deviation in exponential')
print(max(map(abs,list(set(a)-set(c_exp_a)))))
print('b-terms deviation in exponential')
print(max(map(abs,list(set(b)-set(c_exp_b)))))
print('a-terms deviation in double_cosine')
print(max(map(abs,list(set(A)-set(c_double_cosine_a)))))
print('b-terms deviation in double_cosine')
print(max(map(abs,list(set(B)-set(c_double_cosine_b)))))
