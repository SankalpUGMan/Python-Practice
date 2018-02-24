import numpy
import matplotlib.pyplot as plt
import math
import scipy.special as spe
from pylab import *

def bessel(t, v):
	j = (sqrt(2/(math.pi)*t))*(numpy.cos(t-v*(math.pi)/2-(math.pi)/4))
	return j	

x = linspace(0,20,41)
print(x[len(x)-1])

m = bessel(x, 1)
print(m)

def funct_call(t, u, model):
	if (model == 1):	
		w = list()
		v = list()
		d = []
		y = linspace(0.5, t[len(t)-1], 2*t[len(t)-1])
		k = u
		for k in y:
			z = linspace(k, t[len(t)-1], (t[len(t)-1])/k)
	    		l = len(z)
	    		P = numpy.zeros((l,2))
	    		P[:,0] = numpy.cos(z)
	    		P[:,1] = numpy.sin(z)
	    		b = spe.jv(1,z)
	    		c = lstsq(P,b,rcond=-1)[0]
	    		A = c[0]
	    		B = c[1]
	    		p = (A/(numpy.sqrt(A**2+B**2)))
	    		f = numpy.arccos(p)
	    		w.append(f)
	    		v = ((2*f)/(numpy.pi)-(1/2))
			d.append(v)

		plt.figure(1)
		plt.plot(y,d,'ro')
		plt.xlabel('x')
		plt.ylabel('v')
		plt.title('Plot of all v values')
		plt.grid(True)
		plt.show()

	if (model == 2):	
		w = list()
		v = list()
		d = []
		y = linspace(0.5, t[len(t)-1], 2*t[len(t)-1])
		k = u
		for k in y:
			z = linspace(k, t[len(t)-1], (t[len(t)-1])/k)
	    		l = len(z)
	    		P = numpy.zeros((l,2))
	    		P[:,0] = numpy.cos(z)/(numpy.sqrt(z))
	    		P[:,1] = numpy.sin(z)/(numpy.sqrt(z))
	    		b = spe.jv(1,z)
	    		c = lstsq(P,b,rcond=-1)[0]
	    		A = c[0]
	    		B = c[1]
	    		p = (A/(numpy.sqrt(A**2+B**2)))
	    		f = numpy.arccos(p)
	    		w.append(f)
	    		v = ((2*f)/(numpy.pi)-(1/2))
			d.append(v)

		plt.figure(2)
		plt.plot(y,d,'ro')
		plt.xlabel('x')
		plt.ylabel('v')
		plt.title('Plot of all v values b y method 2')
		plt.grid(True)
		plt.show()

s = funct_call(x, 1 , 1)
print(s)
