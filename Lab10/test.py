import math
from pylab import *
import numpy
import random
import matplotlib.pyplot as plt
"""
t = linspace(-pi,pi,65)
print len(t)
f = sin(sqrt(2)*t)
g = fftshift(f)
S = numpy.zeros((64, 16))
print S
print S.shape
"""

t = linspace(-pi,pi,65)
t = t[:-1]
y = sin(sqrt(2)*t)
y[0] = 0                                                             
y = fftshift(y)                                                      
Y = fftshift(fft(y))/64.0
print Y.shape
print type(Y)
Z = Y.transpose()
print Z.shape

a = np.array([1, 2])
print a
print a.shape

f = a.transpose()
print f 
print f.shape

"""
figure(0)
plt.plot(t,f)
plt.show()

figure(1)
plt.plot(t,g)
plt.show()

delta = numpy.random.randn(len(t))
print delta

DELTA = random.randrange(1,3)
print DELTA
"""
