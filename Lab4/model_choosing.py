import numpy
import matplotlib.pyplot as plt
import math
import scipy.special as spe
from pylab import *

def bessel(t, v):
	j = (sqrt(2/(math.pi)*t))*(numpy.cos(t-v*(math.pi)/2-(math.pi)/4))
	return j	

x = linspace(0,40,81)

def calcnu(x, x0, model):
	if (model == 'b'):	
		w = list()
		v = list()
		d = []
		q = linspace(x0,40,81)					# we are giving x by ourselves
		for k in q:
			z = numpy.arange(k, x[len(x)-1] + 0.5 ,0.5)     # I have added + 0.5 in x[len(x)-1] because numpy.arange takes upper limit as nearest integer
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
	    		v = (f - (math.pi)/4)*(2/(math.pi))
			d.append(v)

		plt.figure(1)
		plt.plot(x,d,'ro')
		plt.xlabel('x')
		plt.ylabel('v')
		plt.title('Plot of all v values through model b')
		plt.grid(True)
		plt.show()

	if (model == 'c'):	
		w = list()
		v = list()
		d = []
		q = linspace(x0,40,81)					
		for k in q:
			z = numpy.arange(k, x[len(x)-1] + 0.5 ,0.5)    
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
	    		v = (f - (math.pi)/4)*(2/(math.pi))
			d.append(v)

		plt.figure(1)
		plt.plot(x,d,'ro')
		plt.xlabel('x')
		plt.ylabel('v')
		plt.title('Plot of all v values through model c')
		plt.grid(True)
		plt.show()

s = calcnu(x, 0.5, 'b')
t = calcnu(x, 0.5, 'c')
print(s)
print(t)
