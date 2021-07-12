from scipy.stats import geninvgauss
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

p, b = 2.3, 1.5
mean, var, skew, kurt = geninvgauss.stats(p, b, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(geninvgauss.ppf(0.01, p, b),
                geninvgauss.ppf(0.99, p, b), 100)
ax.plot(x, geninvgauss.pdf(x, p, b),
       'r-', lw=5, alpha=0.6, label='geninvgauss pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = geninvgauss(p, b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = geninvgauss.ppf([0.001, 0.5, 0.999], p, b)
np.allclose([0.001, 0.5, 0.999], geninvgauss.cdf(vals, p, b))
# True

# Generate random numbers:

r = geninvgauss.rvs(p, b, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
