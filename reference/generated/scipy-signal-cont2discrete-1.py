# We can transform a continuous state-space system to a discrete one:

import matplotlib.pyplot as plt
from scipy.signal import cont2discrete, lti, dlti, dstep

# Define a continuous state-space system.

A = np.array([[0, 1],[-10., -3]])
B = np.array([[0],[10.]])
C = np.array([[1., 0]])
D = np.array([[0.]])
l_system = lti(A, B, C, D)
t, x = l_system.step(T=np.linspace(0, 5, 100))
fig, ax = plt.subplots()
ax.plot(t, x, label='Continuous', linewidth=3)

# Transform it to a discrete state-space system using several methods.

dt = 0.1
for method in ['zoh', 'bilinear', 'euler', 'backward_diff', 'foh', 'impulse']:
   d_system = cont2discrete((A, B, C, D), dt, method=method)
   s, x_d = dstep(d_system)
   ax.step(s, np.squeeze(x_d), label=method, where='post')
ax.axis([t[0], t[-1], x[0], 1.4])
ax.legend(loc='best')
fig.tight_layout()
plt.show()
