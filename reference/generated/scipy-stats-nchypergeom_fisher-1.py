from scipy.stats import nchypergeom_fisher
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

M, n, N, odds = 140, 80, 60, 0.5
mean, var, skew, kurt = nchypergeom_fisher.stats(M, n, N, odds, moments='mvsk')

# Display the probability mass function (``pmf``):

x = np.arange(nchypergeom_fisher.ppf(0.01, M, n, N, odds),
              nchypergeom_fisher.ppf(0.99, M, n, N, odds))
ax.plot(x, nchypergeom_fisher.pmf(x, M, n, N, odds), 'bo', ms=8, label='nchypergeom_fisher pmf')
ax.vlines(x, 0, nchypergeom_fisher.pmf(x, M, n, N, odds), colors='b', lw=5, alpha=0.5)

# Alternatively, the distribution object can be called (as a function)
# to fix the shape and location. This returns a "frozen" RV object holding
# the given parameters fixed.

# Freeze the distribution and display the frozen ``pmf``:

rv = nchypergeom_fisher(M, n, N, odds)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()

# Check accuracy of ``cdf`` and ``ppf``:

prob = nchypergeom_fisher.cdf(x, M, n, N, odds)
np.allclose(x, nchypergeom_fisher.ppf(prob, M, n, N, odds))
# True

# Generate random numbers:

r = nchypergeom_fisher.rvs(M, n, N, odds, size=1000)
