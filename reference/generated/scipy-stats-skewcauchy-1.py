from scipy.stats import skewcauchy
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

a = 0.5
mean, var, skew, kurt = skewcauchy.stats(a, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(skewcauchy.ppf(0.01, a),
                skewcauchy.ppf(0.99, a), 100)
ax.plot(x, skewcauchy.pdf(x, a),
       'r-', lw=5, alpha=0.6, label='skewcauchy pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = skewcauchy(a)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = skewcauchy.ppf([0.001, 0.5, 0.999], a)
np.allclose([0.001, 0.5, 0.999], skewcauchy.cdf(vals, a))
# True

# Generate random numbers:

r = skewcauchy.rvs(a, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
