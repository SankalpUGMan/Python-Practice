from scipy.integrate import quad
from pylab import *
from matplotlib import pyplot as plt
import numpy

def func(t):
	m = 1/(1+(numpy.multiply(t, t)))
	return m

x = arange(0, 10.1, 0.01)
h = 0.01
y = func(x)
z = cumsum(y)
w = [-y[0]/2 for m in range(len(x))]

def integ(p):
	i = int(p/h)
	a = y[0:i]
	b = z[0:i]
	c = w[0:i]	
	v = h*(b-(a/2) + c)
	s = cumsum(v)[i-1]
	
	#r = cumsum(s)
	#d = r[i-1]
	return s

e = integ(3)
print(e)

