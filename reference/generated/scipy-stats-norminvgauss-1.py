from scipy.stats import norminvgauss
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

a, b = 1.25, 0.5
mean, var, skew, kurt = norminvgauss.stats(a, b, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(norminvgauss.ppf(0.01, a, b),
                norminvgauss.ppf(0.99, a, b), 100)
ax.plot(x, norminvgauss.pdf(x, a, b),
       'r-', lw=5, alpha=0.6, label='norminvgauss pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = norminvgauss(a, b)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = norminvgauss.ppf([0.001, 0.5, 0.999], a, b)
np.allclose([0.001, 0.5, 0.999], norminvgauss.cdf(vals, a, b))
# True

# Generate random numbers:

r = norminvgauss.rvs(a, b, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
