# First a basic example to demonstrate the outputs:

from scipy import stats
data = [6, 9, 12, 7, 8, 8, 13]
mean, var, std = stats.bayes_mvs(data)
mean
# Mean(statistic=9.0, minmax=(7.103650222612533, 10.896349777387467))
var
# Variance(statistic=10.0, minmax=(3.176724206..., 24.45910382...))
std
# Std_dev(statistic=2.9724954732045084, minmax=(1.7823367265645143, 4.945614605014631))

# Now we generate some normally distributed random data, and get estimates of
# mean and standard deviation with 95% confidence intervals for those
# estimates:

n_samples = 100000
data = stats.norm.rvs(size=n_samples)
res_mean, res_var, res_std = stats.bayes_mvs(data, alpha=0.95)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(data, bins=100, density=True, label='Histogram of data')
ax.vlines(res_mean.statistic, 0, 0.5, colors='r', label='Estimated mean')
ax.axvspan(res_mean.minmax[0],res_mean.minmax[1], facecolor='r',
           alpha=0.2, label=r'Estimated mean (95% limits)')
ax.vlines(res_std.statistic, 0, 0.5, colors='g', label='Estimated scale')
ax.axvspan(res_std.minmax[0],res_std.minmax[1], facecolor='g', alpha=0.2,
           label=r'Estimated scale (95% limits)')

ax.legend(fontsize=10)
ax.set_xlim([-4, 4])
ax.set_ylim([0, 0.5])
plt.show()
