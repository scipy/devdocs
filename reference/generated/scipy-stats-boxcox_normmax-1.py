from scipy import stats
import matplotlib.pyplot as plt

# We can generate some data and determine the optimal ``lmbda`` in various
# ways:

rng = np.random.default_rng()
x = stats.loggamma.rvs(5, size=30, random_state=rng) + 5
y, lmax_mle = stats.boxcox(x)
lmax_pearsonr = stats.boxcox_normmax(x)

lmax_mle
# 1.4613865614008015
lmax_pearsonr
# 1.6685004886804342
stats.boxcox_normmax(x, method='all')
# array([1.66850049, 1.46138656])

fig = plt.figure()
ax = fig.add_subplot(111)
prob = stats.boxcox_normplot(x, -10, 10, plot=ax)
ax.axvline(lmax_mle, color='r')
ax.axvline(lmax_pearsonr, color='g', ls='--')

plt.show()

# Alternatively, we can define our own `optimizer` function. Suppose we
# are only interested in values of `lmbda` on the interval [6, 7], we
# want to use `scipy.optimize.minimize_scalar` with ``method='bounded'``,
# and we want to use tighter tolerances when optimizing the log-likelihood
# function. To do this, we define a function that accepts positional argument
# `fun` and uses `scipy.optimize.minimize_scalar` to minimize `fun` subject
# to the provided bounds and tolerances:

from scipy import optimize
options = {'xatol': 1e-12}  # absolute tolerance on `x`
def optimizer(fun):
    return optimize.minimize_scalar(fun, bounds=(6, 7),
                                    method="bounded", options=options)
stats.boxcox_normmax(x, optimizer=optimizer)
# 6.000...
