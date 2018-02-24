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

step=[0.05]
vec = (numpy.linspace(0,5,(5/step[-1]) +1))     			#this vector consists of the values through which our integration algorithm must pass for final answer

array = func(vec)
s = numpy.cumsum(array)

exact_integ = numpy.arctan(vec)

integ_1 = step[-1]*(s-0.5*(func(x(1,0,step[-1]))+array))

max_error = numpy.amax(integ_1)                                		#max_error initialized
true_error = np.amax(abs(exact_integ-integ_1))

estimate=list()                      				 	#list to store max_error
exact=[true_error]

while max_error > 1e-8:                           		 	#condition of >10^(-8)
    stepi=(step[-1])/2                        	 			#step size halved(last element of 'step' list)
    vec_new = (numpy.linspace(0,5,(5/stepi) +1))  		 	#new vector based on the new step size formed
    array_new = func(vec_new)
    s=numpy.cumsum(array_new)
    integ_2 = stepi*(s-0.5*(func(x(1,0,stepi))+array_new))       	#integral values at new step size formed
    tan_def = numpy.arctan(vec_new)
    comm = numpy.nonzero(numpy.in1d(vec_new,vec))[0]         		#getting indices of the common points between previous and new array
    integ_cmp = integ_2[comm]                             		#new array to store the intgrals at those common points with halved h value
    max_error = numpy.amax(abs(integ_1-integ_cmp))               	#finding max_error with difference(estimated error)
    true_error = numpy.amax(abs(integ_2-tan_def))
    estimate.append(max_error)                                		#appending the estimated error to array 'diff'
    exact.append(true_error)	
    integ_1 = integ_2                                     	 	#now for interation the inte_2 becomes inte_1
    vec = vec_new                                      		 	#vec_new becomes vec
    array = array_new                                      		#arr_new becomes arr
    step.append(stepi)

estimate.append(0)                                               	#this is the buffer value being appended becoz estim will end at one value less as it sees future error is less than    								threshold


plt.figure(0)
plt.plot(step,exact,'ro')
plt.plot(step,estimate,'g+')
plt.yscale("log")
plt.xscale("log")
plt.xlabel('h')
plt.ylabel('Error')
plt.legend(('Exact Error'),('Estimated Error'))
plt.show()
