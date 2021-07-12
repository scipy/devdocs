# An impulse at the 0th element (:math:`\delta[n]`):

from scipy import signal
signal.unit_impulse(8)
# array([ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])

# Impulse offset by 2 samples (:math:`\delta[n-2]`):

signal.unit_impulse(7, 2)
# array([ 0.,  0.,  1.,  0.,  0.,  0.,  0.])

# 2-dimensional impulse, centered:

signal.unit_impulse((3, 3), 'mid')
# array([[ 0.,  0.,  0.],
# [ 0.,  1.,  0.],
# [ 0.,  0.,  0.]])

# Impulse at (2, 2), using broadcasting:

signal.unit_impulse((4, 4), 2)
# array([[ 0.,  0.,  0.,  0.],
# [ 0.,  0.,  0.,  0.],
# [ 0.,  0.,  1.,  0.],
# [ 0.,  0.,  0.,  0.]])

# Plot the impulse response of a 4th-order Butterworth lowpass filter:

imp = signal.unit_impulse(100, 'mid')
b, a = signal.butter(4, 0.2)
response = signal.lfilter(b, a, imp)

import matplotlib.pyplot as plt
plt.plot(np.arange(-50, 50), imp)
plt.plot(np.arange(-50, 50), response)
plt.margins(0.1, 0.1)
plt.xlabel('Time [samples]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
