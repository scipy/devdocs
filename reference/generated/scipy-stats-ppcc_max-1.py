# First we generate some random data from a Weibull distribution
# with shape parameter 2.5:

from scipy import stats
import matplotlib.pyplot as plt
rng = np.random.default_rng()
c = 2.5
x = stats.weibull_min.rvs(c, scale=4, size=2000, random_state=rng)

# Generate the PPCC plot for this data with the Weibull distribution.

fig, ax = plt.subplots(figsize=(8, 6))
res = stats.ppcc_plot(x, c/2, 2*c, dist='weibull_min', plot=ax)

# We calculate the value where the shape should reach its maximum and a
# red line is drawn there. The line should coincide with the highest
# point in the PPCC graph.

cmax = stats.ppcc_max(x, brack=(c/2, 2*c), dist='weibull_min')
ax.axvline(cmax, color='r')
plt.show()
