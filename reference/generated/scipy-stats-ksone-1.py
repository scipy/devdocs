from scipy.stats import ksone
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

n = 1e+03
mean, var, skew, kurt = ksone.stats(n, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(ksone.ppf(0.01, n),
                ksone.ppf(0.99, n), 100)
ax.plot(x, ksone.pdf(x, n),
       'r-', lw=5, alpha=0.6, label='ksone pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = ksone(n)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = ksone.ppf([0.001, 0.5, 0.999], n)
np.allclose([0.001, 0.5, 0.999], ksone.cdf(vals, n))
# True

# Generate random numbers:

r = ksone.rvs(n, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
