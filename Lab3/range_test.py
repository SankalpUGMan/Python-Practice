 # coding: utf-8

from scipy.integrate import quad
from pylab import *
from matplotlib import pyplot as plt
import numpy
from scipy import *

for i in range(1,25):			#in for loops second limit is not counted
	print(i)

m = linspace(0,49,50)			#in linspace 1st and 2nd limits both are counted. In linspace we specify the number of points.
print(m)

c = numpy.arange(25)			#numpy.arange also does not count second limit
print(c)
