#Analysis of circuits using Laplace Transforms

#Importing modules and libraries

import pylab as py
import numpy
import math
import matplotlib.pyplot as plt
import scipy.signal as sp
from sympy import *

#Creating a function and solving the matrices for the low pass filter

s = symbols('s')
def lowpass(R1,R2,C1,C2,G,Vi):
    A = Matrix([[0,0,1,-1/G],[(-1)/(1+s*R2*C2),1,0,0],[0,-G,G,1],[((-1)/(R1))-(1/R2)-s*C1,1/R2,0,s*C1]])
    b = Matrix([0,0,0,Vi/R1])
    V = A.inv()*b
    return (A,b,V)

#Obtaining output voltage, H(jw) graph for the low pass filter and plotting

A,b,V = lowpass(10000,10000,1e-9,1e-9,1.586,1)
Vo = V[3]
w = py.logspace(0,8,801)
ss = 1j*w
hf = lambdify(s,Vo,'numpy')
v = hf(ss)

plt.figure(0)
py.loglog(w,abs(v),lw = 2)
py.title('Bode plot of the step response of the output voltage \n for the low pass filter using matrices')
py.xlabel('frequency (omega)')
py.ylabel('H')
py.grid(True)
py.show()

#Getting impulse response of the low pass filter

Vo = simplify(Vo)
num, denom = fraction(Vo)
Num = Poly(num,s)
Denom = Poly(denom,s)
num_coeff = Num.all_coeffs()
denom_coeff = Denom.all_coeffs()
num_coeff=[float(i) for i in num_coeff]
denom_coeff=[float(i) for i in denom_coeff]
H_num1 = numpy.poly1d(num_coeff)
H_denom1 = numpy.poly1d(denom_coeff)
H_1 = sp.lti(H_num1, H_denom1)
t_vo_low, h1 = sp.impulse(H_1, None, numpy.linspace(0,1e2,1e5))

#Plotting impulse response of the low pass filter

plt.figure(1)
plt.plot(t_vo_low,h1)
plt.title('Plot of impulse response of the low pass filter')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.show()

#Obtaining vo(t) from the transfer function of a low pass filter when a given function is the input

t_vo1 = numpy.linspace(0,0.05,1e5)			
vi = numpy.sin(2000*(math.pi)*t_vo1) + numpy.cos(2*(1e6)*(math.pi)*t_vo1)					
t_transfer1, vo1, vec_transfer1 = sp.lsim(H_1, vi, t_vo1)

#Plotting vo(t) for the low pass filter

plt.figure(2)	
plt.plot(t_vo1, vo1)
plt.title('Plot of output voltage of the circuit calculated from the transfer function \n for a given input to a low pass filter')
plt.xlabel('t')
plt.ylabel('vo(t)')
plt.show()

#Creating function and solving the matrices for the high pass filter

s = symbols('s')
def highpass(R1,R3,C1,C2,G,Vi):
	A = Matrix([[0,0,1,-1/G],[-s*C2,s*C2+1/R3,0,0],[0,G,-G,-1],[1/R1+s*C2+s*C1,-s*C2,0,-1/R1]])
	b = Matrix([0,0,0,s*C1*Vi])
	V = A.inv()*b
	return (A,b,V)

#Obtaining output voltage, H(jw) graph for the high pass filter and plotting

A,b,V = highpass(10000,10000,1e-9,1e-9,1.586,1)
Vo = V[3]
w = py.logspace(0,8,801)
ss = 1j*w
hf = lambdify(s,Vo,'numpy')
v = hf(ss)

plt.figure(3)
py.loglog(w,abs(v),lw=2)
py.title('Bode plot of the step response of the output voltage \n for the high pass filter using matrices')
py.xlabel('frequency (omega)')
py.ylabel('H')
py.grid(True)
py.show()

#Getting impulse response of the high pass filter

Vo = simplify(Vo)
num, denom = fraction(Vo)
Num = Poly(num,s)
Denom = Poly(denom,s)
num_coeff = Num.all_coeffs()
denom_coeff = Denom.all_coeffs()
num_coeff=[float(i) for i in num_coeff]
denom_coeff=[float(i) for i in denom_coeff]
H_num2 = numpy.poly1d(num_coeff)
H_denom2 = numpy.poly1d(denom_coeff)
H_2 = sp.lti(H_num2, H_denom2)
t_vo_high, h2 = sp.impulse(H_2, None, numpy.linspace(0,1e-4,1e5))

#Plotting impulse response of the low pass filter

plt.figure(4)
plt.plot(t_vo_high,h2)
plt.title('Plot of impulse response of the high pass filter')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.show()

#Obtaining vo(t) from the transfer function of a high pass filter when a given function is the input

t_vo2 = numpy.linspace(0,5e-5,1e4)			
vi = numpy.sin(2000*(math.pi)*t_vo2) + numpy.cos(2*(1e6)*(math.pi)*t_vo2)					
t_transfer2, vo2, vec_transfer2 = sp.lsim(H_2, vi, t_vo2)

#Plotting vo(t) for the high pass filter

plt.figure(5)	
plt.plot(t_vo2, vo2)
plt.title('Plot of output voltage of the circuit calculated from the transfer function \n for a given input to a high pass filter')
plt.xlabel('t')
plt.ylabel('vo(t)')
plt.show()

#Obtaining the repsonse of the circuit for a damped sinusoidal input

t_vo3 = numpy.linspace(0,0.1,1e5)		
vi2 = numpy.exp(-50*t_vo3)*(numpy.sin(500*(math.pi)*t_vo3))
t_transfer3, vo3, vec_transfer3 = sp.lsim(H_2, vi2, t_vo3)

#Plotting output of the damped input

plt.figure(6)	
plt.plot(t_vo3, vo3, 'b')
plt.title('Plot of output voltage of the circuit for a damped sinusoidal input, vo(t) \n alpha = 50, frequency = 250')
plt.xlabel('t')
plt.ylabel('vo(t)')
plt.show()

#Obtaining the repsonse of the circuit for a unit step response

Vi_damp_num = numpy.poly1d([1])
Vi_damp_denom = numpy.poly1d([1,0])	
Vi_damp = sp.lti(Vi_damp_num, Vi_damp_denom)
t_vo4, vi3 = sp.impulse(Vi_damp, None, numpy.linspace(0,1e-4,1e5))
vi3[0] = 0		
t_transfer4, vo4, vec_transfer4 = sp.lsim(H_2, vi3, t_vo4)

#Plotting output of the unit step input

plt.figure(5)	
plt.plot(t_vo4, vo4)
plt.title('Plot of response of the circuit for a unit step input')
plt.xlabel('t')
plt.ylabel
('vo(t)')
plt.show()
