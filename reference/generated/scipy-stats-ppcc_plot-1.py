# First we generate some random data from a Weibull distribution
# with shape parameter 2.5, and plot the histogram of the data:

from scipy import stats
import matplotlib.pyplot as plt
rng = np.random.default_rng()
c = 2.5
x = stats.weibull_min.rvs(c, scale=4, size=2000, random_state=rng)

# Take a look at the histogram of the data.

fig1, ax = plt.subplots(figsize=(9, 4))
ax.hist(x, bins=50)
ax.set_title('Histogram of x')
plt.show()

# Now we explore this data with a PPCC plot as well as the related
# probability plot and Box-Cox normplot.  A red line is drawn where we
# expect the PPCC value to be maximal (at the shape parameter ``c``
# used above):

fig2 = plt.figure(figsize=(12, 4))
ax1 = fig2.add_subplot(1, 3, 1)
ax2 = fig2.add_subplot(1, 3, 2)
ax3 = fig2.add_subplot(1, 3, 3)
res = stats.probplot(x, plot=ax1)
res = stats.boxcox_normplot(x, -4, 4, plot=ax2)
res = stats.ppcc_plot(x, c/2, 2*c, dist='weibull_min', plot=ax3)
ax3.axvline(c, color='r')
plt.show()
