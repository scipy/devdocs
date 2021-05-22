from scipy.stats import zipfian
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

a, n = 1.25, 10
mean, var, skew, kurt = zipfian.stats(a, n, moments='mvsk')

# Display the probability mass function (``pmf``):

x = np.arange(zipfian.ppf(0.01, a, n),
              zipfian.ppf(0.99, a, n))
ax.plot(x, zipfian.pmf(x, a, n), 'bo', ms=8, label='zipfian pmf')
ax.vlines(x, 0, zipfian.pmf(x, a, n), colors='b', lw=5, alpha=0.5)

# Alternatively, the distribution object can be called (as a function)
# to fix the shape and location. This returns a "frozen" RV object holding
# the given parameters fixed.

# Freeze the distribution and display the frozen ``pmf``:

rv = zipfian(a, n)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()

# Check accuracy of ``cdf`` and ``ppf``:

prob = zipfian.cdf(x, a, n)
np.allclose(x, zipfian.ppf(prob, a, n))
# True

# Generate random numbers:

r = zipfian.rvs(a, n, size=1000)

# Confirm that `zipfian` reduces to `zipf` for large `n`, `a > 1`.

from scipy.stats import zipf
k = np.arange(11)
np.allclose(zipfian.pmf(k, a=3.5, n=10000000), zipf.pmf(k, a=3.5))
# True
