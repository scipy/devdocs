from scipy.stats import betabinom
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

n, a, b = 5, 2.3, 0.63
mean, var, skew, kurt = betabinom.stats(n, a, b, moments='mvsk')

# Display the probability mass function (``pmf``):

x = np.arange(betabinom.ppf(0.01, n, a, b),
              betabinom.ppf(0.99, n, a, b))
ax.plot(x, betabinom.pmf(x, n, a, b), 'bo', ms=8, label='betabinom pmf')
ax.vlines(x, 0, betabinom.pmf(x, n, a, b), colors='b', lw=5, alpha=0.5)

# Alternatively, the distribution object can be called (as a function)
# to fix the shape and location. This returns a "frozen" RV object holding
# the given parameters fixed.

# Freeze the distribution and display the frozen ``pmf``:

rv = betabinom(n, a, b)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()

# Check accuracy of ``cdf`` and ``ppf``:

prob = betabinom.cdf(x, n, a, b)
np.allclose(x, betabinom.ppf(prob, n, a, b))
# True

# Generate random numbers:

r = betabinom.rvs(n, a, b, size=1000)
