import numpy
import matplotlib.pyplot as plt
import math
import scipy.special as spe
from pylab import *

def bessel(t, v):
	j = (sqrt(2/(math.pi)*t))*(numpy.cos(t-v*(math.pi)/2-(math.pi)/4))
	return j	

x = linspace(0,20,41)
print(x)
m = bessel(x, 1)
for i in range(0, len(x)):
	print('%s : %f'% (i, m[i]))

plt.plot(x,m,'#000000')
plt.xlabel('x')
plt.ylabel('Jv(x)')
plt.title('Graph of Bessel function of first type')
plt.show()
