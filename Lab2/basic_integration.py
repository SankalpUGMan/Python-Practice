from scipy.integrate import quad
from pylab import *
from matplotlib import pyplot as plt
import numpy

def func(t):
	m = 1/(1+(numpy.multiply(t, t)))
	return m

x = arange(0, 100.1, 0.01)
h = 0.01

y = func(x)
print(y)

def integ(p):
	if (p == 0):
		I = 0
	elif (p != 0):
		add = 0
		i = int(p/h)
		for j in y[0:i]:
			add = add + j
			final = []
			final.append(h*((add)-0.5*(y[0]) - 0.5*(y[i])))
			I = 0
			for l in final:
				I = I + l
					
	return I

r = float(integ(2))
print(r)
s = float(integ(5))
print(s)
