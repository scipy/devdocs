# Compute the waveform with instantaneous frequency::

# f(t) = 0.025*t**3 - 0.36*t**2 + 1.25*t + 2

# over the interval 0 <= t <= 10.

from scipy.signal import sweep_poly
p = np.poly1d([0.025, -0.36, 1.25, 2.0])
t = np.linspace(0, 10, 5001)
w = sweep_poly(t, p)

# Plot it:

import matplotlib.pyplot as plt
plt.subplot(2, 1, 1)
plt.plot(t, w)
plt.title("Sweep Poly\nwith frequency " +
          "$f(t) = 0.025t^3 - 0.36t^2 + 1.25t + 2$")
plt.subplot(2, 1, 2)
plt.plot(t, p(t), 'r', label='f(t)')
plt.legend()
plt.xlabel('t')
plt.tight_layout()
plt.show()
