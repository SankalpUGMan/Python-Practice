from scipy import *
from matplotlib.pylab import *
import time as t
				
t3=t.time()			# time the block
x=rand(100000)
ii=where(x>0.999) 		# find locations where x>0.999
w=x[ii] 			# create new vector with only those values
print w
t4=t.time()
print "the program took %.3f seconds to find %d randoms" % (t4-t3,len(w))
