from scipy.stats import yulesimon
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

alpha = 11
mean, var, skew, kurt = yulesimon.stats(alpha, moments='mvsk')

# Display the probability mass function (``pmf``):

x = np.arange(yulesimon.ppf(0.01, alpha),
              yulesimon.ppf(0.99, alpha))
ax.plot(x, yulesimon.pmf(x, alpha), 'bo', ms=8, label='yulesimon pmf')
ax.vlines(x, 0, yulesimon.pmf(x, alpha), colors='b', lw=5, alpha=0.5)

# Alternatively, the distribution object can be called (as a function)
# to fix the shape and location. This returns a "frozen" RV object holding
# the given parameters fixed.

# Freeze the distribution and display the frozen ``pmf``:

rv = yulesimon(alpha)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()

# Check accuracy of ``cdf`` and ``ppf``:

prob = yulesimon.cdf(x, alpha)
np.allclose(x, yulesimon.ppf(prob, alpha))
# True

# Generate random numbers:

r = yulesimon.rvs(alpha, size=1000)
