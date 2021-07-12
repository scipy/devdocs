from scipy.stats import kappa4
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

h, k = 0.1, 0
mean, var, skew, kurt = kappa4.stats(h, k, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(kappa4.ppf(0.01, h, k),
                kappa4.ppf(0.99, h, k), 100)
ax.plot(x, kappa4.pdf(x, h, k),
       'r-', lw=5, alpha=0.6, label='kappa4 pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = kappa4(h, k)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = kappa4.ppf([0.001, 0.5, 0.999], h, k)
np.allclose([0.001, 0.5, 0.999], kappa4.cdf(vals, h, k))
# True

# Generate random numbers:

r = kappa4.rvs(h, k, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
