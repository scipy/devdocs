from scipy.stats import laplace_asymmetric
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

kappa = 2
mean, var, skew, kurt = laplace_asymmetric.stats(kappa, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(laplace_asymmetric.ppf(0.01, kappa),
                laplace_asymmetric.ppf(0.99, kappa), 100)
ax.plot(x, laplace_asymmetric.pdf(x, kappa),
       'r-', lw=5, alpha=0.6, label='laplace_asymmetric pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = laplace_asymmetric(kappa)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = laplace_asymmetric.ppf([0.001, 0.5, 0.999], kappa)
np.allclose([0.001, 0.5, 0.999], laplace_asymmetric.cdf(vals, kappa))
# True

# Generate random numbers:

r = laplace_asymmetric.rvs(kappa, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
