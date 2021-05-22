# We'll use `lsim` to simulate an analog Bessel filter applied to
# a signal.

from scipy.signal import bessel, lsim
import matplotlib.pyplot as plt

# Create a low-pass Bessel filter with a cutoff of 12 Hz.

b, a = bessel(N=5, Wn=2*np.pi*12, btype='lowpass', analog=True)

# Generate data to which the filter is applied.

t = np.linspace(0, 1.25, 500, endpoint=False)

# The input signal is the sum of three sinusoidal curves, with
# frequencies 4 Hz, 40 Hz, and 80 Hz.  The filter should mostly
# eliminate the 40 Hz and 80 Hz components, leaving just the 4 Hz signal.

u = (np.cos(2*np.pi*4*t) + 0.6*np.sin(2*np.pi*40*t) +
     0.5*np.cos(2*np.pi*80*t))

# Simulate the filter with `lsim`.

tout, yout, xout = lsim((b, a), U=u, T=t)

# Plot the result.

plt.plot(t, u, 'r', alpha=0.5, linewidth=1, label='input')
plt.plot(tout, yout, 'k', linewidth=1.5, label='output')
plt.legend(loc='best', shadow=True, framealpha=1)
plt.grid(alpha=0.3)
plt.xlabel('t')
plt.show()

# In a second example, we simulate a double integrator ``y'' = u``, with
# a constant input ``u = 1``.  We'll use the state space representation
# of the integrator.

from scipy.signal import lti
A = np.array([[0.0, 1.0], [0.0, 0.0]])
B = np.array([[0.0], [1.0]])
C = np.array([[1.0, 0.0]])
D = 0.0
system = lti(A, B, C, D)

# `t` and `u` define the time and input signal for the system to
# be simulated.

t = np.linspace(0, 5, num=50)
u = np.ones_like(t)

# Compute the simulation, and then plot `y`.  As expected, the plot shows
# the curve ``y = 0.5*t**2``.

tout, y, x = lsim(system, u, t)
plt.plot(t, y)
plt.grid(alpha=0.3)
plt.xlabel('t')
plt.show()
