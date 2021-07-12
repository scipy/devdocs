# Create a scipy.stats distribution from a numpy histogram

import scipy.stats
import numpy as np
data = scipy.stats.norm.rvs(size=100000, loc=0, scale=1.5, random_state=123)
hist = np.histogram(data, bins=100)
hist_dist = scipy.stats.rv_histogram(hist)

# Behaves like an ordinary scipy rv_continuous distribution

hist_dist.pdf(1.0)
# 0.20538577847618705
hist_dist.cdf(2.0)
# 0.90818568543056499

# PDF is zero above (below) the highest (lowest) bin of the histogram,
# defined by the max (min) of the original dataset

hist_dist.pdf(np.max(data))
# 0.0
hist_dist.cdf(np.max(data))
# 1.0
hist_dist.pdf(np.min(data))
# 7.7591907244498314e-05
hist_dist.cdf(np.min(data))
# 0.0

# PDF and CDF follow the histogram

import matplotlib.pyplot as plt
X = np.linspace(-5.0, 5.0, 100)
plt.title("PDF from Template")
plt.hist(data, density=True, bins=100)
plt.plot(X, hist_dist.pdf(X), label='PDF')
plt.plot(X, hist_dist.cdf(X), label='CDF')
plt.show()
