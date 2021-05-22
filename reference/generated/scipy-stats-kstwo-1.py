from scipy.stats import kstwo
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

n = 10
mean, var, skew, kurt = kstwo.stats(n, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(kstwo.ppf(0.01, n),
                kstwo.ppf(0.99, n), 100)
ax.plot(x, kstwo.pdf(x, n),
       'r-', lw=5, alpha=0.6, label='kstwo pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = kstwo(n)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = kstwo.ppf([0.001, 0.5, 0.999], n)
np.allclose([0.001, 0.5, 0.999], kstwo.cdf(vals, n))
# True

# Generate random numbers:

r = kstwo.rvs(n, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
