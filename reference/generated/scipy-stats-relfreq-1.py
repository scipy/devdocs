import matplotlib.pyplot as plt
from numpy.random import default_rng
from scipy import stats
rng = default_rng()
a = np.array([2, 4, 1, 2, 3, 2])
res = stats.relfreq(a, numbins=4)
res.frequency
# array([ 0.16666667, 0.5       , 0.16666667,  0.16666667])
np.sum(res.frequency)  # relative frequencies should add up to 1
# 1.0

# Create a normal distribution with 1000 random values

samples = stats.norm.rvs(size=1000, random_state=rng)

# Calculate relative frequencies

res = stats.relfreq(samples, numbins=25)

# Calculate space of values for x

x = res.lowerlimit + np.linspace(0, res.binsize*res.frequency.size,
                                 res.frequency.size)

# Plot relative frequency histogram

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(1, 1, 1)
ax.bar(x, res.frequency, width=res.binsize)
ax.set_title('Relative frequency histogram')
ax.set_xlim([x.min(), x.max()])

plt.show()
