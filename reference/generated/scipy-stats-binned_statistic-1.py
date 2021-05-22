from scipy import stats
import matplotlib.pyplot as plt

# First some basic examples:

# Create two evenly spaced bins in the range of the given sample, and sum the
# corresponding values in each of those bins:

values = [1.0, 1.0, 2.0, 1.5, 3.0]
stats.binned_statistic([1, 1, 2, 5, 7], values, 'sum', bins=2)
# BinnedStatisticResult(statistic=array([4. , 4.5]),
# bin_edges=array([1., 4., 7.]), binnumber=array([1, 1, 1, 2, 2]))

# Multiple arrays of values can also be passed.  The statistic is calculated
# on each set independently:

values = [[1.0, 1.0, 2.0, 1.5, 3.0], [2.0, 2.0, 4.0, 3.0, 6.0]]
stats.binned_statistic([1, 1, 2, 5, 7], values, 'sum', bins=2)
# BinnedStatisticResult(statistic=array([[4. , 4.5],
# [8. , 9. ]]), bin_edges=array([1., 4., 7.]),
# binnumber=array([1, 1, 1, 2, 2]))

stats.binned_statistic([1, 2, 1, 2, 4], np.arange(5), statistic='mean',
                       bins=3)
# BinnedStatisticResult(statistic=array([1., 2., 4.]),
# bin_edges=array([1., 2., 3., 4.]),
# binnumber=array([1, 2, 1, 2, 3]))

# As a second example, we now generate some random data of sailing boat speed
# as a function of wind speed, and then determine how fast our boat is for
# certain wind speeds:

rng = np.random.default_rng()
windspeed = 8 * rng.random(500)
boatspeed = .3 * windspeed**.5 + .2 * rng.random(500)
bin_means, bin_edges, binnumber = stats.binned_statistic(windspeed,
                boatspeed, statistic='median', bins=[1,2,3,4,5,6,7])
plt.figure()
plt.plot(windspeed, boatspeed, 'b.', label='raw data')
plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:], colors='g', lw=5,
           label='binned statistic of data')
plt.legend()

# Now we can use ``binnumber`` to select all datapoints with a windspeed
# below 1:

low_boatspeed = boatspeed[binnumber == 0]

# As a final example, we will use ``bin_edges`` and ``binnumber`` to make a
# plot of a distribution that shows the mean and distribution around that
# mean per bin, on top of a regular histogram and the probability
# distribution function:

x = np.linspace(0, 5, num=500)
x_pdf = stats.maxwell.pdf(x)
samples = stats.maxwell.rvs(size=10000)

bin_means, bin_edges, binnumber = stats.binned_statistic(x, x_pdf,
        statistic='mean', bins=25)
bin_width = (bin_edges[1] - bin_edges[0])
bin_centers = bin_edges[1:] - bin_width/2

plt.figure()
plt.hist(samples, bins=50, density=True, histtype='stepfilled',
         alpha=0.2, label='histogram of data')
plt.plot(x, x_pdf, 'r-', label='analytical pdf')
plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:], colors='g', lw=2,
           label='binned statistic of data')
plt.plot((binnumber - 0.5) * bin_width, x_pdf, 'g.', alpha=0.5)
plt.legend(fontsize=10)
plt.show()
