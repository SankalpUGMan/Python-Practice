from scipy.integrate import quad
from pylab import *
from matplotlib import pyplot as plt
import numpy

def func(t):
	m = 1/(1+numpy.multiply(t,t))
	return m

x = numpy.linspace(0, 5.1, 101)

j = arctan(x)
print(type(j))

# Use this section for plotting integration values
"""
for i in range(0, len(x)):
	integration_ans, integration_error = quad(func, 0 , x[i])
	print(x[i], integration_ans)
	plt.plot(x[i], integration_ans, 'ro')

plt.plot(x[0], 0 , 'ro', label = 'integral plot')
plt.plot(x, j, '#000000', label = 'arctan plot')
plt.xlabel('x')
plt.ylabel(' $\int_{0}^{x} dx/{1+x^{2}}$')
plt.title('Plot of $\int_{0}^{x} dx/{1+x^{2}}$ in red and arctan in black')
plt.legend()
plt.show()
"""

# Use this section for plotting integration errors

integration_ans = numpy.zeros(len(x))

for k,i in zip(x,range(0, len(x))):
	integration_ans[i] = quad(func, 0 , k)[0]
	print(k, integration_ans)

err = abs(integration_ans-j)

plt.semilogy(x, err, 'ro')
plt.xlabel('x')
plt.ylabel('$\int_{0}^{x} dx/{1+x^{2}}$ error')
plt.title('Plot of $\int_{0}^{x} dx/{1+x^{2}}$ error')
plt.show()


