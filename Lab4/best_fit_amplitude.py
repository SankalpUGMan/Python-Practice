import numpy
import matplotlib.pyplot as plt
import math
import scipy.special as spe
from pylab import *

def bessel(t, v):
	j = (sqrt(2/(math.pi)*t))*(numpy.cos(t-v*(math.pi)/2-(math.pi)/4))
	return j	

x = linspace(0,20,41)

w = list()
v = list()
d = []

y = linspace(0.5,18,36)

for k in y:
    z = numpy.arange(k,20.5,0.5)
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

print(v)

plt.figure(2)
plt.plot(y,d,'go')
plt.xlabel('x')
plt.ylabel('v')
plt.title('Plot of all v values')
plt.grid(True)
plt.show()
