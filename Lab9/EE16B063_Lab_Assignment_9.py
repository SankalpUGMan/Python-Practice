#The Digital Fourier Transform

#Importing libraries

from pylab import *
import matplotlib.pyplot as plt
"""
#Calculating fourier and inverse fourier transform

x = rand(100)
X = fft(x)                                                  #forward fourier transform of x
y = ifft(X)                                                 #inverse fourier transform of X
c_[x,y]                                                     #creating a matrix with x and y as columns
print abs(x-y).max()

#Calculating fourier transform for sine function

x = linspace(0,2*pi,128)
y = sin(5*x)
Y = fft(y)

#Plotting

plt.figure(0)
plt.subplot(2,1,1)
plt.plot(abs(Y),lw = 2)
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of $\sin(5t)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(unwrap(angle(Y)),lw = 2)
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$k$",size = 16)
plt.grid(True)
plt.savefig("sine_fourier.png")                              #direct image saving to the folder
plt.show()

#Correcting the errors and rectifying for the sine function

x = linspace(0,2*pi,129)
x = x[:-1]
y = sin(5*x)
Y = fftshift(fft(y))/128.0
w = linspace(-64,63,128)

#Plotting

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw = 2)
plt.xlim([-10,10])
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of $\sin(5t)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
ii = where(abs(Y)>1e-3)
plt.plot(w[ii],angle(Y[ii]),'go',lw = 2)
plt.xlim([-10,10])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$k$",size = 16)
plt.grid(True)
plt.savefig("sine_fourier2.png")
plt.show()

#Obtaining fourier plot for an amplitude modulated signal

t = linspace(0,2*pi,129)
t = t[:-1]
y = (1+0.1*cos(t))*cos(10*t)
Y = fftshift(fft(y))/128.0
w = linspace(-64,63,128)

#Plotting

plt.figure(2)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of $\left(1+0.1\cos\left(t\right)\right)\cos\left(10t\right)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("amp_modulation.png")
plt.show()

#Correcting the errors and rectifying for the amplitude modulated function

t = linspace(-4*pi,4*pi,513)
t = t[:-1]
y = (1+0.1*cos(t))*cos(10*t)
Y = fftshift(fft(y))/512.0
w = linspace(-64,64,513)
w = w[:-1]

#Plotting

plt.figure(3)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of $\left(1+0.1\cos\left(t\right)\right)\cos\left(10t\right)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("amp_modulation2.png")
plt.show()

#Obtaining fourier transform of sin^3(t)

t = linspace(-4*pi,4*pi,513)
t = t[:-1]
y = sin(t)*sin(t)*sin(t)
Y = fftshift(fft(y))/512.0
w = linspace(-64,64,513)
w = w[:-1]

#Plotting

plt.figure(4)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"$|H|$",size = 16)
plt.title(r"Spectrum of sin^3(t)")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
ii = where(abs(Y)>1e-3)
plt.plot(w[ii],angle(Y[ii]),'go',lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $H$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("sine_cube_fourier.png")
plt.show()

#Obtaining fourier transform of cos^3(t)

t = linspace(-4*pi,4*pi,513)
t = t[:-1]
y = cos(t)*cos(t)*cos(t)
Y = fftshift(fft(y))/512.0
w = linspace(-64,64,513)
w = w[:-1]

#Plotting

plt.figure(5)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"$|H|$",size = 16)
plt.title(r"Spectrum of cos^3(t)")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
ii = where(abs(Y)>1e-3)
plt.plot(w[ii],angle(Y[ii]),'go',lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $H$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("cosine_cube_fourier.png")
plt.show()

#Obtaining the spectrum of cos(20t + 5 cos(t))

t = linspace(-4*pi,4*pi,513)
t = t[:-1]
y = cos(20*t + 5*cos(t))
Y = fftshift(fft(y))/512.0
w = linspace(-64,64,513)
w = w[:-1]

#Plotting

plt.figure(6)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw = 2)
plt.xlim([-35,35])
plt.ylabel(r"$|H|$",size = 16)
plt.title(r"Spectrum of cos(20t + 5 cos(t))")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
ii = where(abs(Y)>1e-3)
plt.plot(w[ii],angle(Y[ii]),'go',lw = 2)
plt.xlim([-35,35])
plt.ylabel(r"Phase of $H$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("complex_sinusoid.png")
plt.show()
"""
#Obtaining the spectrum of e^(-t^2/2)

#From python fft function

N = 512
t = linspace(-4*pi,4*pi,N+1)
t = t[:-1]
y = exp(-(t*t)/2)
Y = fftshift(fft(y))/(N)
w = linspace(-64,64,N+1)
w = w[:-1]

#Plotting

plt.figure(7)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"$|H|$",size = 16)
plt.title(r"Spectrum of  e^(-t^2/2) for $\omega$ = (-15,15) calculated from python module")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
ii = where(abs(Y)>1e-3)
plt.plot(w[ii],angle(Y[ii]),'go',lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $H$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("squared_exponential.png")
plt.show()

#Manually

def squared_exponential_fourier(m):
	return ((2*pi)**(0.5))*(e**(-2*pi*pi*m*m))/N

f = squared_exponential_fourier(w)

#Plotting

plt.figure(8)
plt.subplot(2,1,1)
plt.plot(w,f,lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"$|H|$",size = 16)
plt.title(r"Spectrum of  e^(-t^2/2) for $\omega$ = (-15,15) manually")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(f),'ro',lw = 2)
plt.xlim([-15,15])
plt.ylabel(r"Phase of $H$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("squared_exponential2.png")
plt.show()

#Combo plotting

plt.figure(9)
plt.plot(w,abs(Y),'r')
plt.plot(w,f,'b')
plt.xlim([-15,15])
plt.ylabel(r"$|H|$", size = 16)
plt.title(r"Combined fourier spectrum of  e^(-t^2/2) for $\omega$ = (-15,15)")
plt.grid(True)
plt.savefig("squared_exponential_combo.png")
plt.show()

#Error plotting

m = abs(Y-f).max()
n = abs(Y-f)
print m

plt.figure(10)
plt.plot(w,n,'b')
plt.xlim([-15,15])
plt.ylabel(r"$|H|$", size = 16)
plt.title(r"Error plot for $\omega$ = (-15,15)")
plt.grid(True)
plt.savefig("error_plot.png")
plt.show()
