import matplotlib.pyplot as plt
rng = np.random.default_rng()

# First define some input parameters for the signal:

A = 2.
w = 1.
phi = 0.5 * np.pi
nin = 1000
nout = 100000
frac_points = 0.9  # Fraction of points to select

# Randomly select a fraction of an array with timesteps:

r = rng.standard_normal(nin)
x = np.linspace(0.01, 10*np.pi, nin)
x = x[r >= frac_points]

# Plot a sine wave for the selected times:

y = A * np.sin(w*x+phi)

# Define the array of frequencies for which to compute the periodogram:

f = np.linspace(0.01, 10, nout)

# Calculate Lomb-Scargle periodogram:

import scipy.signal as signal
pgram = signal.lombscargle(x, y, f, normalize=True)

# Now make a plot of the input data:

plt.subplot(2, 1, 1)
plt.plot(x, y, 'b+')

# Then plot the normalized periodogram:

plt.subplot(2, 1, 2)
plt.plot(f, pgram)
plt.show()
