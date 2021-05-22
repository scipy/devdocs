from scipy import signal
b = signal.firwin(80, 0.5, window=('kaiser', 8))
w, h = signal.freqz(b)

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')

ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid()
ax2.axis('tight')
plt.show()

# Broadcasting Examples

# Suppose we have two FIR filters whose coefficients are stored in the
# rows of an array with shape (2, 25). For this demonstration, we'll
# use random data:

rng = np.random.default_rng()
b = rng.random((2, 25))

# To compute the frequency response for these two filters with one call
# to `freqz`, we must pass in ``b.T``, because `freqz` expects the first
# axis to hold the coefficients. We must then extend the shape with a
# trivial dimension of length 1 to allow broadcasting with the array
# of frequencies.  That is, we pass in ``b.T[..., np.newaxis]``, which has
# shape (25, 2, 1):

w, h = signal.freqz(b.T[..., np.newaxis], worN=1024)
w.shape
# (1024,)
h.shape
# (2, 1024)

# Now, suppose we have two transfer functions, with the same numerator
# coefficients ``b = [0.5, 0.5]``. The coefficients for the two denominators
# are stored in the first dimension of the 2-D array  `a`::

# a = [   1      1  ]
# [ -0.25, -0.5 ]

b = np.array([0.5, 0.5])
a = np.array([[1, 1], [-0.25, -0.5]])

# Only `a` is more than 1-D. To make it compatible for
# broadcasting with the frequencies, we extend it with a trivial dimension
# in the call to `freqz`:

w, h = signal.freqz(b, a[..., np.newaxis], worN=1024)
w.shape
# (1024,)
h.shape
# (2, 1024)
