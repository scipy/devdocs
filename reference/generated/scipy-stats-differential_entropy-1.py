from scipy.stats import differential_entropy, norm

# Entropy of a standard normal distribution:

rng = np.random.default_rng()
values = rng.standard_normal(100)
differential_entropy(values)
# 1.3407817436640392

# Compare with the true entropy:

float(norm.entropy())
# 1.4189385332046727

# For several sample sizes between 5 and 1000, compare the accuracy of
# the ``'vasicek'``, ``'van es'``, and ``'ebrahimi'`` methods. Specifically,
# compare the root mean squared error (over 1000 trials) between the estimate
# and the true differential entropy of the distribution.

from scipy import stats
import matplotlib.pyplot as plt
# >>>
# >>>
def rmse(res, expected):
    '''Root mean squared error'''
    return np.sqrt(np.mean((res - expected)**2))
# >>>
# >>>
a, b = np.log10(5), np.log10(1000)
ns = np.round(np.logspace(a, b, 10)).astype(int)
reps = 1000  # number of repetitions for each sample size
expected = stats.expon.entropy()
# >>>
method_errors = {'vasicek': [], 'van es': [], 'ebrahimi': []}
for method in method_errors:
    for n in ns:
       rvs = stats.expon.rvs(size=(reps, n), random_state=rng)
       res = stats.differential_entropy(rvs, method=method, axis=-1)
       error = rmse(res, expected)
       method_errors[method].append(error)
# >>>
for method, errors in method_errors.items():
    plt.loglog(ns, errors, label=method)
# >>>
plt.legend()
plt.xlabel('sample size')
plt.ylabel('RMSE (1000 trials)')
plt.title('Entropy Estimator Error (Exponential Distribution)')
