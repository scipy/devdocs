from scipy.stats import crystalball
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

beta, m = 2, 3
mean, var, skew, kurt = crystalball.stats(beta, m, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(crystalball.ppf(0.01, beta, m),
                crystalball.ppf(0.99, beta, m), 100)
ax.plot(x, crystalball.pdf(x, beta, m),
       'r-', lw=5, alpha=0.6, label='crystalball pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = crystalball(beta, m)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = crystalball.ppf([0.001, 0.5, 0.999], beta, m)
np.allclose([0.001, 0.5, 0.999], crystalball.cdf(vals, beta, m))
# True

# Generate random numbers:

r = crystalball.rvs(beta, m, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
