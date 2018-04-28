from pylab import *

a = range(2,5) 						 #in such array declarations, we have the first number in our array but not the last one. We have one number before it 								 available. Range accept integer arguments. So, if we enter some float arguments, they are converted to ints.
print(a)

b = ones((3,3))
print(b)

c = a*b
print(c)

d = dot(a,b)   						  #This dot thing does actual multiplication of matrices
print(d)

e = array(([3],[4],[1],[5]), dtype = complex)
print(e)

print(c.size)   					  #list elements don't have size, shape but has length
print(c.shape)
print(len(a))

k = [5 for i in range(7)]            			  # This is a great technique to make all the elements of a list equal to a particular number. 
print(k) 
