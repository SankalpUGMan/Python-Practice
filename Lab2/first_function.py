from pylab import *

def func(t):
	m = 1/(1+(float(t)**2))
	return m

print(func(3))	

x = arange(0, 5.1, 0.1)

for i in range(0, len(x)):
	print(x[i], func(x[i]))
