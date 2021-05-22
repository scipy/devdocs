from scipy.stats import kappa3
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

a = 1
mean, var, skew, kurt = kappa3.stats(a, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(kappa3.ppf(0.01, a),
                kappa3.ppf(0.99, a), 100)
ax.plot(x, kappa3.pdf(x, a),
       'r-', lw=5, alpha=0.6, label='kappa3 pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = kappa3(a)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = kappa3.ppf([0.001, 0.5, 0.999], a)
np.allclose([0.001, 0.5, 0.999], kappa3.cdf(vals, a))
# True

# Generate random numbers:

r = kappa3.rvs(a, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
