#The Tubelight Model

#Importing libraries and modules

import numpy
import math
import matplotlib.pyplot as plt
from pylab import *
import sys
from tabulate import tabulate

#Declaring parameters

#n = 100				#grid size, i.e partitions of the tubelight
n = int(sys.argv[1])
#M = 5					#number of electrons emitted in each turn
M = int(sys.argv[2])
#nk = 500				#number of times simulation is done
nk = int(sys.argv[3])
#u0 = 5					#threshold velocity
u0 = float(sys.argv[4])
#p = 0.25				#probability of ionization
p = float(sys.argv[5])
#sigma = 2				#sigma of the probability distribution function
sigma = float(sys.argv[6])		
#m = 5					#mean of the probability distribution function
m = float(sys.argv[7])                   

#Declaring vectors to hold electron information while iterating

xx = numpy.zeros(n*M)			#electron position
u = numpy.zeros(n*M)			#electron velocity
dx = numpy.zeros(n*M)			#displacement current

#Declaring vectors to hold electron information after iteration

I = []					#intensity of emitted light
X = []					#electron position
V = []					#electron velocity

#Iterating

for k in range(1,nk):
		m = abs(int(numpy.random.randn()*sigma + m))                          #creating electrons
		hh = numpy.where(xx == 0)[0]					      #finding the location where position of the electron is zero
		m_slots = numpy.random.choice(hh,m)				      #finding the location of electrons and making its position value 1
		xx[m_slots] = 1		
					       
		ii = numpy.where(xx>0)[0]					      #finding indices where xx>0
		dx[ii] = u[ii] + 0.5						      #updating the position and velocity of the electron
		xx = xx + dx
		u[ii] = u[ii] + 1
		
		jj = numpy.where(xx>=n)[0]					      #putting constraints on the electrons whose position went beyond n
		xx[jj] = 0
		dx[jj] = 0
		u[jj] = 0

		kk = numpy.where(u>=u0)[0]					      #indices where velocity of the electron is greater than the threshold
		ll = numpy.where(rand(len(kk))<=p)[0]				      #indices of the electrons which have the probability of collision
		kl = kk[ll]							      #indices of the electrons which are colliding
		u[kl] = 0							      #setting the velocity of electron as zero after the inelastic collision
		xx[kl] = xx[kl] - dx[kl]*(rand(len(xx[kl])))			      #finding the location of collision

		I.extend(xx[kl].tolist())					      #appending to the lists
		X.extend(xx[ii].tolist())
		V.extend(u[ii].tolist())

#Plotting

figure(0)
plt.hist(X,101,edgecolor='green')
plt.xlabel('Partitions of the tubelight')
plt.ylabel('Electron Density')
plt.title('Population plot of the electron position \n n = %d , M = %d , nk = %d, u0 = %d, p = %0.02f, sigma = %0.02f , m = %0.02f' %(n, M, nk, u0, p, sigma, m))
plt.show()

figure(1)
#hist = (population, bins, data)
pop_count, bins, rect = plt.hist(I, 101, edgecolor = 'red')
plt.xlabel('Partitions of the tubelight')
plt.ylabel('Intensity plot')
plt.title('Population plot of the electron intensity \n n = %d , M = %d , nk = %d, u0 = %d, p = %0.02f, sigma = %0.02f , m = %0.02f' %(n, M, nk, u0, p, sigma, m))
plt.show()

figure(2)
plt.plot(X, V, 'rx')
plt.xlabel('Velocity of electrons')
plt.ylabel('Position of electrons')
plt.title('Electron phase space \n n = %d , M = %d , nk = %d, u0 = %d, p = %0.02f, sigma = %0.02f , m = %0.02f' %(n, M, nk, u0, p, sigma, m))
plt.show()

#Creating the table

x_pos = 0.5*(bins[0:-1] + bins[1:])							#converting to mid-point values

li = list()
print ("Intensity Data")
first_row = ["xpos", "Count"]
for pos, co in zip(x_pos,pop_count):
	l_temp = [pos,co]
	li.append(l_temp)
li.insert(0, first_row)
print(tabulate(li,tablefmt = 'psql', headers = "firstrow"))
