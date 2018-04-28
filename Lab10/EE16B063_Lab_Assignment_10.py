#Spectra of non-periodic signals

#Importing libraries

from pylab import *
import numpy
import math
import random
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes

#Obtaining fourier transform of sin(sqrt(2*t))

t = linspace(-pi,pi,65)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
y = sin(sqrt(2)*t)
y[0] = 0                                                             #the sample corresponding to -tmax should be set zero
y = fftshift(y)                                                      #make y start with y(t=0)
Y = fftshift(fft(y))/64.0
w = linspace(-pi*fmax,pi*fmax,65)
w = w[:-1]

#Plotting

plt.figure(0)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw = 2)
plt.xlim([-10,10])
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of $\sin\left(\sqrt{2}t\right)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-10,10])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("sine_root2t_fourier.png")
plt.show()

#Plotting for several time periods

t1 = linspace(-pi,pi,65)
t1 = t1[:-1]
t2 = linspace(-3*pi,-pi,65)
t2 = t2[:-1]
t3 = linspace(pi,3*pi,65)
t3 = t3[:-1]
#y = sin(sqrt(2)*t)

#Plotting

plt.figure(1)
plt.plot(t1,sin(sqrt(2)*t1),'b',lw = 2)
plt.plot(t2,sin(sqrt(2)*t2),'r',lw = 2)
plt.plot(t3,sin(sqrt(2)*t3),'r',lw = 2)
plt.ylabel(r"$y$",size = 16)
plt.xlabel(r"$t$",size = 16)
plt.title(r"$\sin\left(\sqrt{2}t\right)$")
plt.grid(True)
plt.savefig("many_time_periods.png")
plt.show()

#Replicating required part

t1 = linspace(-pi,pi,65)
t1 = t1[:-1]
t2 = linspace(-3*pi,-pi,65)
t2 = t2[:-1]
t3 = linspace(pi,3*pi,65)
t3 = t3[:-1]
y = sin(sqrt(2)*t1)

#Plotting

plt.figure(2)
plt.plot(t1,y,'bo',lw = 2)
plt.plot(t2,y,'ro',lw = 2)
plt.plot(t3,y,'ro',lw = 2)
plt.ylabel(r"$y$",size = 16)
plt.xlabel(r"$t$",size = 16)
plt.title(r"$\sin\left(\sqrt{2}t\right)$ with $t$ wrapping every $2\pi$ ")
plt.grid(True)
plt.savefig("replication.png")
plt.show()

#Obtaining ramp

t = linspace(-pi,pi,65)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
y = t
y[0] = 0                                                                   #the sample corresponding to -tmax should be set zero
y = fftshift(y)                                                            #make y start with y(t=0)
Y = fftshift(fft(y))/64.0
w = linspace(-pi*fmax,pi*fmax,65)
w = w[:-1]

#Plotting

plt.figure(3)
plt.semilogx(abs(w),20*log10(abs(Y)),lw = 2)
plt.xlim([1,10])
plt.ylim([-20,0])
plt.xticks([1,2,5,10],["1","2","5","10"],size = 16)
plt.ylabel(r"$|Y|$ (dB)",size = 16)
plt.title(r"Spectrum of a digital ramp")
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("ramp.png")
plt.show()

#Windowing

t1 = linspace(-pi,pi,65)
t1 = t1[:-1]
t2 = linspace(-3*pi,-pi,65)
t2 = t2[:-1]
t3 = linspace(pi,3*pi,65)
t3 = t3[:-1]
n = arange(64)
wnd = fftshift(0.54+0.46*cos(2*pi*n/63))
y = sin(sqrt(2)*t1)*wnd

#Plotting

plt.figure(4)
plt.plot(t1,y,'bo',lw = 2)
plt.plot(t2,y,'ro',lw = 2)
plt.plot(t3,y,'ro',lw = 2)
plt.ylabel(r"$y$",size = 16)
plt.xlabel(r"$t$",size = 16)
plt.title(r"$\sin\left(\sqrt{2}t\right)\times w(t)$ with $t$ wrapping every $2\pi$ ")
plt.grid(True)
plt.savefig("windowing.png")
plt.show()

#Windowed fourier response

t = linspace(-pi,pi,65)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
n = arange(64)
wnd = fftshift(0.54+0.46*cos(2*pi*n/63))
y = sin(sqrt(2)*t)*wnd
y[0] = 0                                                                                 #the sample corresponding to -tmax should be set zero
y = fftshift(y)                                                                          #make y start with y(t=0)
Y = fftshift(fft(y))/64.0
w = linspace(-pi*fmax,pi*fmax,65)
w = w[:-1]

#Plotting

plt.figure(5)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),lw = 2)
plt.xlim([-8,8])
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of $\sin\left(\sqrt{2}t\right)\times w(t)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-8,8])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("windowed_fourier.png")
plt.show()

#Increased points plotting

t = linspace(-4*pi,4*pi,257)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
n = arange(256)
wnd = fftshift(0.54+0.46*cos(2*pi*n/256))
y = sin(sqrt(2)*t)
y = y*wnd
y[0] = 0                                                                                     #the sample corresponding to -tmax should be set zero
y = fftshift(y)                                                                              #make y start with y(t=0)
Y = fftshift(fft(y))/256.0
w = linspace(-pi*fmax,pi*fmax,257)
w = w[:-1]

#Plotting

plt.figure(6)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),'b',w,abs(Y),'bo',lw = 2)
plt.xlim([-4,4])
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of $\sin\left(\sqrt{2}t\right)\times w(t)$")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-4,4])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("many_points_windowed_fourier.png")
plt.show()

#Spectrum of cos cubed t with Hamming window

t = linspace(-8*pi,8*pi,513)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
n = arange(512)
wnd = fftshift(0.54+0.46*cos(2*pi*n/512))
y = cos(0.86*t)*cos(0.86*t)*cos(0.86*t)
y = y*wnd
y[0] = 0                                                                                     
y = fftshift(y)                                                                              
Y = fftshift(fft(y))/512.0
w = linspace(-pi*fmax,pi*fmax,513)
w = w[:-1]

#Plotting

plt.figure(7)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),'b',w,abs(Y),'bo',lw = 2)
plt.xlim([-5,5])
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of cos^3(t)")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-5,5])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("cos_cubed_ham.png")
plt.show()

#Spectrum of cos cubed t without Hamming window

t = linspace(-8*pi,8*pi,513)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
y = cos(0.86*t)*cos(0.86*t)*cos(0.86*t)
y[0] = 0                                                                                     
y = fftshift(y)                                                                              
Y = fftshift(fft(y))/512.0
w = linspace(-pi*fmax,pi*fmax,513)
w = w[:-1]

#Plotting

plt.figure(8)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),'b',w,abs(Y),'bo',lw = 2)
plt.xlim([-5,5])
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of cos^3(t)")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-5,5])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("cos_cubed_non-ham.png")
plt.show()

#Spectrum of cos(omega*t + delta)

t = linspace(-2*pi,2*pi,129)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
delta = numpy.random.randn(len(t))
y = cos(t + delta)                                                      #I took omega as 1
n = arange(128)
wnd = fftshift(0.54+0.46*cos(2*pi*n/128))
y = y*wnd
y[0] = 0                                                                                     
y = fftshift(y)                                                                              
Y = fftshift(fft(y))/128.0
w = linspace(-pi*fmax,pi*fmax,129)
w = w[:-1]

#Plotting

plt.figure(9)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),'b',w,abs(Y),'bo',lw = 2)
plt.xlim([-5,5])
plt.ylabel(r"$|Y|$",size = 16)
plt.title('Spectrum of cos(wt + d) \n omega = 1')
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-5,5])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("cos(wt + delta).png")
plt.show()

#Spectrum of cos(omega*t + delta) with white gaussian noise

t = linspace(-2*pi,2*pi,129)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
delta = numpy.random.randn(len(t))
y = cos(t + delta) + 0.1*numpy.random.randn(len(t))                                                      #I took omega as 1
n = arange(128)
wnd = fftshift(0.54+0.46*cos(2*pi*n/128))
y = y*wnd
y[0] = 0                                                                                     
y = fftshift(y)                                                                              
Y = fftshift(fft(y))/128.0
w = linspace(-pi*fmax,pi*fmax,129)
w = w[:-1]

#Plotting

plt.figure(10)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),'b',w,abs(Y),'bo',lw = 2)
plt.xlim([-5,5])
plt.ylabel(r"$|Y|$",size = 16)
plt.title('Spectrum of cos(wt + d) with noise \n omega = 1')
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-5,5])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("cos(wt + delta) with noise.png")
plt.show()

#Spectrum of chirped signal

t = linspace(-pi,pi,1025)
t = t[:-1]
dt = t[1]-t[0]
fmax = 1/dt
y = cos(16*(1.5 + t/(2*pi))*t)
y[0] = 0                                                                                     
y = fftshift(y)                                                                              
Y = fftshift(fft(y))/1024.0
w = linspace(-pi*fmax,pi*fmax,1025)
w = w[:-1]

#Plotting

plt.figure(11)
plt.subplot(2,1,1)
plt.plot(w,abs(Y),'b',w,abs(Y),'bo',lw = 1)
plt.xlim([-50,50])
plt.ylabel(r"$|Y|$",size = 16)
plt.title(r"Spectrum of chirped signal")
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(w,angle(Y),'ro',lw = 2)
plt.xlim([-50,50])
plt.ylabel(r"Phase of $Y$",size = 16)
plt.xlabel(r"$\omega$",size = 16)
plt.grid(True)
plt.savefig("chirped signal.png")
plt.show()

#Getting dft for a range of frequencies and obtaining the surface plot

S = numpy.zeros((63, 63))
t_plot = linspace(-pi,pi,64)
t_plot = t_plot[:-1]
dt_plot = t_plot[1]-t_plot[0]
fmax_plot = 1/dt_plot
w_plot = linspace(-pi*fmax_plot,pi*fmax_plot,64)
w_plot = w_plot[:-1]

for k in range(0,15):
	t = linspace((-(8-k)*pi)/8,(-(7-k)*pi)/8, 64) 
	t = t[:-1]
	y = cos(16*(1.5 + t/(2*pi))*t)
	y[0] = 0
	y = fftshift(y)                                                                              
	Y = fftshift(fft(y))/64
	S[:,k] = Y.transpose()

#Plotting the surface plot

figure = figure(12)
plotting = axes.Axes3D(figure) 									#Axes3D is the means to do a surface plot
plt.title('The 3-D surface plot of chirped function')
surf = plotting.plot_surface(t_plot, w_plot, abs(S).T, rstride=1, cstride=1, cmap=cm.jet)
plt.show()
