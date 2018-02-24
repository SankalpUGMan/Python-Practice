from scipy.integrate import quad
from pylab import *
from matplotlib import pyplot as plt
import numpy

def ex(r1, r2):
	t = linspace(r1,r2,1000) 
	m = numpy.exp(t)
	plt.figure(1)
	plt.semilogy(t, m, 'ro', label = 'exponential function')
	plt.xlabel('x')
	plt.ylabel('$e^x$')
	plt.title('Plot of exponential function')
	plt.grid(True)
	plt.legend()
	plt.show()

def double_cos(r1, r2):
	t = linspace(r1,r2,1000)
	n = numpy.cos(cos(t))
	plt.figure(2)	
	plt.plot(t, n, 'ro', label = 'double cosine')
	plt.xlabel('x')
	plt.ylabel('$cos(cos(x))$')
	plt.title('Plot of double cosine function')
	plt.grid(True)
	plt.legend()
	plt.show()

y = ex(-2*(math.pi), 4*(math.pi))
z = double_cos(-2*(math.pi), 4*(math.pi))


