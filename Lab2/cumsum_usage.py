from scipy.integrate import quad
from pylab import *
from matplotlib import pyplot as plt
import numpy

def func(t):
	m = 1/(1+(numpy.multiply(t, t)))
	return m

def x(k,a,h):
	n = a + k*h
    	return n

step = 0.01        				   #step size
vec = (numpy.linspace(0,5,(5/step) +1),object)     #this vector consists of the values through which our integration algorithm must pass for final answer

array = func(vec[0])				 
s = numpy.cumsum(array)

integration = step*(s-0.5*(func(x(1,0,step))+array))

ans = numpy.where(vec[0]==1)
print(integration[ans])

plt.figure(0)
plt.plot(vec[0],integration,'ro')
plt.xlabel('x')
plt.ylabel(' $\int_{0}^{x} dx/{1+x^{2}}$')
plt.title('Plot of $\int_{0}^{x} dx/{1+x^{2}}$ using cumsum')
plt.show()

