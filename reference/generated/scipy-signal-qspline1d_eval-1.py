# We can filter a signal to reduce and smooth out high-frequency noise with
# a quadratic spline:

import matplotlib.pyplot as plt
from scipy.signal import qspline1d, qspline1d_eval
rng = np.random.default_rng()
sig = np.repeat([0., 1., 0.], 100)
sig += rng.standard_normal(len(sig))*0.05  # add noise
time = np.linspace(0, len(sig))
filtered = qspline1d_eval(qspline1d(sig), time)
plt.plot(sig, label="signal")
plt.plot(time, filtered, label="filtered")
plt.legend()
plt.show()
