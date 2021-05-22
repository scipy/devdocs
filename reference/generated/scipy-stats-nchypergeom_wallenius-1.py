from scipy.stats import nchypergeom_wallenius
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

M, n, N, odds = 140, 80, 60, 0.5
mean, var, skew, kurt = nchypergeom_wallenius.stats(M, n, N, odds, moments='mvsk')

# Display the probability mass function (``pmf``):

x = np.arange(nchypergeom_wallenius.ppf(0.01, M, n, N, odds),
              nchypergeom_wallenius.ppf(0.99, M, n, N, odds))
ax.plot(x, nchypergeom_wallenius.pmf(x, M, n, N, odds), 'bo', ms=8, label='nchypergeom_wallenius pmf')
ax.vlines(x, 0, nchypergeom_wallenius.pmf(x, M, n, N, odds), colors='b', lw=5, alpha=0.5)

# Alternatively, the distribution object can be called (as a function)
# to fix the shape and location. This returns a "frozen" RV object holding
# the given parameters fixed.

# Freeze the distribution and display the frozen ``pmf``:

rv = nchypergeom_wallenius(M, n, N, odds)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()

# Check accuracy of ``cdf`` and ``ppf``:

prob = nchypergeom_wallenius.cdf(x, M, n, N, odds)
np.allclose(x, nchypergeom_wallenius.ppf(prob, M, n, N, odds))
# True

# Generate random numbers:

r = nchypergeom_wallenius.rvs(M, n, N, odds, size=1000)
