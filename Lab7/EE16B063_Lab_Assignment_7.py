#The Laplace Transform

#Importing modules and libraries

import numpy
from pylab import *
import math
import matplotlib.pyplot as plt
import scipy.signal as sp

#Obtaining f(t)

F_num = poly1d([1,0.5])
F_denom = poly1d([1,1,2.5])
F = sp.lti(F_num, F_denom)
t_f, f = sp.impulse(F, None, linspace(0,50,1001))

#Plotting f(t)

figure(0)
plt.plot(t_f,f)
plt.title('Plot of f(t)')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.show()

#Obtaining x(t)

X_num = F_num
X_denom = polymul([1,0,2.25], F_denom)
X = sp.lti(X_num, X_denom)
t_x, x = sp.impulse(X, None, linspace(0,50,1001))
x[0] = 0

#Plotting x(t)

figure(1)
plt.plot(t_x,x)
plt.title('Plot of x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()

#Obtaining new f(t)

F_new_num = poly1d([1,0.05])
F_new_denom = poly1d([1,0.1,2.2525])
F_new = sp.lti(F_new_num, F_new_denom)
t_new_f, f_new = sp.impulse(F_new, None, linspace(0,50,1001))

#Plotting new f(t)

figure(2)
plt.plot(t_new_f,f_new)
plt.title('Plot of new f(t)')
plt.xlabel('t')
plt.ylabel('New f(t)')
plt.show()

#Obtaining new x(t)

X_new_num = F_new_num
X_new_denom = polymul([1,0,2.25], F_new_denom)
X_new = sp.lti(X_new_num, X_new_denom)
t_new_x, x_new = sp.impulse(X_new, None, linspace(0,50,1001))
x_new[0] = 0

#Plotting new x(t)

figure(3)
plt.plot(t_new_x,x_new)
plt.title('Plot of new x(t)')
plt.xlabel('t')
plt.ylabel('New x(t)')
plt.show()

#Obtaining x(t) from sp.lsim

H = sp.lti(polymul(X_num,F_denom), polymul(X_denom, F_num))
t_in = linspace(0,50,1001)
t_sim, x_sim, vec = sp.lsim(H, f, t_in)

#Plotting x(t) obtained from sp.lsim

figure(4)
plt.plot(t_sim, x_sim)
plt.title('Plot of x(t) obtained using sp.lsim')
plt.xlabel('t')
plt.ylabel('x(t) (obtained from sp.lsim)')
plt.show()

#Plotting in for loop

omega = linspace(1.4, 1.6, 5)

for i in omega:
	F_new_num2 = poly1d([1,0.05])
	F_new_denom2 = poly1d([1,0.1,i*i + 0.0025])
	F_new2 = sp.lti(F_new_num2, F_new_denom2)
	t_new_f2, f_new2 = sp.impulse(F_new2, None, linspace(0,50,1001))
	t = linspace(0,50,1001)
	t_new_sim, x_sim2, vec_sim = sp.lsim(H,f_new2, t)
	figure(5)
	plt.plot(t_new_sim, x_sim2, label = '%s frequency' %i)
	plt.title('Plot of x(t) with varying frequencies \n The values across colored lines are the cosine frequencies')
	plt.xlabel('t')
	plt.ylabel('Varying x(t)')
	plt.legend()
plt.show()	

#Solving the coupled equations and getting x(t) and y(t)

X_coup_num = poly1d([1, 0, 2])
X_coup_denom = poly1d([1,0,3,0])
X_coup = sp.lti(X_coup_num, X_coup_denom)
Y_coup_num = poly1d([2])
Y_coup_denom = poly1d([1,0,3,0])
Y_coup = sp.lti(Y_coup_num, Y_coup_denom)
t_coup_x, x_coup = sp.impulse(X_coup, None, linspace(0,20,1001))
t_coup_y, y_coup = sp.impulse(Y_coup, None, linspace(0,20,1001))

#Plotting x(t) and y(t) from the coupled equations

figure(6)
plt.plot(t_coup_x, x_coup)
plt.title('Plot of x(t) obtained after solving coupled equations')
plt.xlabel('t')
plt.ylabel('Coupled x(t)')
plt.show()

figure(7)
plt.plot(t_coup_y, y_coup)
plt.title('Plot of y(t) obtained after solving coupled equations')
plt.xlabel('t')
plt.ylabel('Coupled y(t)')
plt.show()

#Solving for the steady state response of the two port network

T = sp.lti(poly1d([1]), poly1d([10**-12, 10**-4, 1]))
omega_transfer, mag, phi = T.bode()

#Plotting the magnitude and phase of the transfer function

figure(8)
plt.subplot(2,1,1)
plt.semilogx(omega_transfer, mag)
plt.title('Plot of magnitude and phase of the transfer function')
plt.xlabel('w in log scale')
plt.ylabel('Magnitude')
plt.subplot( 2,1,2)
plt.semilogx(omega_transfer, phi)
plt.xlabel('w in log scale')
plt.ylabel('Phase')
plt.show()

#Obtaining vo of the function

t_vo = linspace(0,0.01,100001)			
vi = cos((10**3)*t_vo) - cos((10**6)*t_vo)					
t_transfer, vo, vec_transfer = sp.lsim(T, vi, t_vo)

#Plotting vo

figure(9)
plt.plot(t_transfer, vo)
plt.title('Plot of Vo')
plt.xlabel('t')
plt.ylabel('Vo(t)')
plt.show()
