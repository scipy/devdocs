# Compute the impulse response of a second order system with a repeated
# root: ``x''(t) + 2*x'(t) + x(t) = u(t)``

from scipy import signal
system = ([1.0], [1.0, 2.0, 1.0])
t, y = signal.impulse(system)
import matplotlib.pyplot as plt
plt.plot(t, y)
