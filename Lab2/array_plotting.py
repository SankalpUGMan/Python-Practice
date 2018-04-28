from pylab import *
from matplotlib import pyplot as plt

def func(t):
	m = 1/(1+(float(t)**2))
	return m

x = arange(0, 5.1, 0.1)

for i in range(0, len(x)):
	plot(x[i], func(x[i]), 'ro')

plt.title('Plot of $1/(1+x^{2})$')
plt.xlabel('x')
plt.ylabel('$1/(1+x^{2})$')
plt.show()
