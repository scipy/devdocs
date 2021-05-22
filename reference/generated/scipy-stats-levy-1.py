from scipy.stats import levy
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

mean, var, skew, kurt = levy.stats(moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(levy.ppf(0.01),
                levy.ppf(0.99), 100)
ax.plot(x, levy.pdf(x),
       'r-', lw=5, alpha=0.6, label='levy pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = levy()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = levy.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], levy.cdf(vals))
# True

# Generate random numbers:

r = levy.rvs(size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
