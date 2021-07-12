from scipy.stats import loguniform
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

a, b = 0.01, 1.25
mean, var, skew, kurt = loguniform.stats(a, b, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(loguniform.ppf(0.01, a, b),
                loguniform.ppf(0.99, a, b), 100)
ax.plot(x, loguniform.pdf(x, a, b),
       'r-', lw=5, alpha=0.6, label='loguniform pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = loguniform(a, b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = loguniform.ppf([0.001, 0.5, 0.999], a, b)
np.allclose([0.001, 0.5, 0.999], loguniform.cdf(vals, a, b))
# True

# Generate random numbers:

r = loguniform.rvs(a, b, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

# This doesn't show the equal probability of ``0.01``, ``0.1`` and
# ``1``. This is best when the x-axis is log-scaled:

import numpy as np
fig, ax = plt.subplots(1, 1)
ax.hist(np.log10(r))
ax.set_ylabel("Frequency")
ax.set_xlabel("Value of random variable")
ax.xaxis.set_major_locator(plt.FixedLocator([-2, -1, 0]))
ticks = ["$10^{{ {} }}$".format(i) for i in [-2, -1, 0]]
ax.set_xticklabels(ticks)  # doctest: +SKIP
plt.show()

# This random variable will be log-uniform regardless of the base chosen for
# ``a`` and ``b``. Let's specify with base ``2`` instead:

rvs = loguniform(2**-2, 2**0).rvs(size=1000)

# Values of ``1/4``, ``1/2`` and ``1`` are equally likely with this random
# variable.  Here's the histogram:

fig, ax = plt.subplots(1, 1)
ax.hist(np.log2(rvs))
ax.set_ylabel("Frequency")
ax.set_xlabel("Value of random variable")
ax.xaxis.set_major_locator(plt.FixedLocator([-2, -1, 0]))
ticks = ["$2^{{ {} }}$".format(i) for i in [-2, -1, 0]]
ax.set_xticklabels(ticks)  # doctest: +SKIP
plt.show()
