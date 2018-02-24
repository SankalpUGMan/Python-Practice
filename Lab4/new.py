from pylab import *
from matplotlib import pyplot as plt
import numpy
from scipy import *
import scipy.special as spe

def bessel(t, v):
	j = spe.jv(v,t)
	return j	

x = arange(0,20.5,0.5)
m = bessel(x, 1)
p = arange(0.5, 18.5, 0.5)

a = numpy.zeros((len(x), len(p)))
J = numpy.zeros((len(x), len(p)))
r = numpy.zeros((len(x), 2*len(p)))
d = numpy.zeros((len(x), 2))
f = numpy.zeros((2, len(p)))
h = numpy.zeros((1, len(p)))
q = numpy.zeros((0, len(p)))

for j in range(0,len(p)):
		for i in range(0, len(x)):
			if x[i] >= p[j]:
				a[i-j-1][j] = x[i]

for j in range(0,len(p)):
		for i in range(0, len(x)):
			J[i][j] = bessel(a[i][j], 1)
print(J)
c = cos(a)
s = sin(a)
print(c)
print(s)
for k in range(0,len(p)):
	r[:,2*k] = c[:,k]
	r[:,2*k + 1] = s[:,k]
	d[:,0] = r[:,2*k]
	d[:,1] = r[:,2*k+1]
	f = lstsq(d, J)[0]
print(f)
print(f.shape)
q = []

for j in range(0,len(p)):
	h[:,j] = f[0,j]/numpy.sqrt((f[0,j]**2+f[1,j]**2))
	q.append((numpy.arccos(h[:,j])-(math.pi)/4)*(2/math.pi))
print(q)

plt.figure(1)
plt.plot(p, q, 'ro')
plt.xlabel('x')
plt.ylabel('v')
plt.title('Plot of v values')
plt.grid(True)
plt.show()
