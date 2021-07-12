from scipy.stats import genhyperbolic
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

p, a, b = 0.5, 1.5, -0.5
mean, var, skew, kurt = genhyperbolic.stats(p, a, b, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(genhyperbolic.ppf(0.01, p, a, b),
                genhyperbolic.ppf(0.99, p, a, b), 100)
ax.plot(x, genhyperbolic.pdf(x, p, a, b),
       'r-', lw=5, alpha=0.6, label='genhyperbolic pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = genhyperbolic(p, a, b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = genhyperbolic.ppf([0.001, 0.5, 0.999], p, a, b)
np.allclose([0.001, 0.5, 0.999], genhyperbolic.cdf(vals, p, a, b))
# True

# Generate random numbers:

r = genhyperbolic.rvs(p, a, b, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
