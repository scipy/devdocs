from scipy.stats import moyal
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

mean, var, skew, kurt = moyal.stats(moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(moyal.ppf(0.01),
                moyal.ppf(0.99), 100)
ax.plot(x, moyal.pdf(x),
       'r-', lw=5, alpha=0.6, label='moyal pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = moyal()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = moyal.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], moyal.cdf(vals))
# True

# Generate random numbers:

r = moyal.rvs(size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
