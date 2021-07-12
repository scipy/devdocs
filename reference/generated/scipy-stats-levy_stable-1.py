from scipy.stats import levy_stable
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

alpha, beta = 1.8, -0.5
mean, var, skew, kurt = levy_stable.stats(alpha, beta, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(levy_stable.ppf(0.01, alpha, beta),
                levy_stable.ppf(0.99, alpha, beta), 100)
ax.plot(x, levy_stable.pdf(x, alpha, beta),
       'r-', lw=5, alpha=0.6, label='levy_stable pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = levy_stable(alpha, beta)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = levy_stable.ppf([0.001, 0.5, 0.999], alpha, beta)
np.allclose([0.001, 0.5, 0.999], levy_stable.cdf(vals, alpha, beta))
# True

# Generate random numbers:

r = levy_stable.rvs(alpha, beta, size=1000)

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
