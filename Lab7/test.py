from scipy import signal

system = ([1.0], [1.0, 2.0, 1.0])
t, y = signal.impulse2(system)

print t
print y
