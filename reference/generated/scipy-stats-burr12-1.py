from scipy.stats import burr12
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

c, d = 10, 4
mean, var, skew, kurt = burr12.stats(c, d, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(burr12.ppf(0.01, c, d),
                burr12.ppf(0.99, c, d), 100)
ax.plot(x, burr12.pdf(x, c, d),
       'r-', lw=5, alpha=0.6, label='burr12 pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = burr12(c, d)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = burr12.ppf([0.001, 0.5, 0.999], c, d)
np.allclose([0.001, 0.5, 0.999], burr12.cdf(vals, c, d))
# True

# Generate random numbers:

r = burr12.rvs(c, d, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
