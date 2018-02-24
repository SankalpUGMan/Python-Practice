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
	n = numpy.cos(cos(x))
	v = n*cos(k*x)
	return v

def double_cosine_sine(x,k):
	n = numpy.cos(cos(x))
	v = n*sin(k*x)
	return v

print('Below are exp_cosine coefficient values')

for i in range(0,51):
	e = quad(exp_cosine, 0, 2*(math.pi), args=(i))[0]
	print('%d : %f'% (i, e))

print('Below are exp_sine coefficient values')

for j in range(0,51):
	f = quad(exp_sine, 0, 2*(math.pi), args=(j))[0]
	print('%d : %f'% (j, f))

print('Below are double_cosine_cosine coefficient values')

for k in range(0,51):
	g = quad(double_cosine_cosine, 0, 2*(math.pi), args = (k))[0]
	print('%d : %f'% (k, g))

print('Below are double_cosine_sine coefficient values')

for l in range(0,51):
	h = quad(double_cosine_cosine, 0, 2*(math.pi), args = (l))[0]
	print('%d : %f'% (l, h))



