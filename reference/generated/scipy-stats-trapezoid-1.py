from scipy.stats import trapezoid
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

c, d = 0.2, 0.8
mean, var, skew, kurt = trapezoid.stats(c, d, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(trapezoid.ppf(0.01, c, d),
                trapezoid.ppf(0.99, c, d), 100)
ax.plot(x, trapezoid.pdf(x, c, d),
       'r-', lw=5, alpha=0.6, label='trapezoid pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = trapezoid(c, d)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = trapezoid.ppf([0.001, 0.5, 0.999], c, d)
np.allclose([0.001, 0.5, 0.999], trapezoid.cdf(vals, c, d))
# True

# Generate random numbers:

r = trapezoid.rvs(c, d, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
