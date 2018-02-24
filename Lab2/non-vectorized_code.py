from pylab import *
import time as t

t1=t.time()									# time the calculations with for loop
n=0
w=zeros(200) 									# we don't expect to see more than 200 randoms
for i in range(100000):
	x=rand(1)
	if x>0.999:
		w[n]=x
		n+=1
t2=t.time()
w=w[0:n]
print w
print "the program took %.3f seconds to find %d randoms" % (t2-t1,len(w))
