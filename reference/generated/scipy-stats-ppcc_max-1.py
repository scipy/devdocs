# First we generate some random data from a Tukey-Lambda distribution,
# with shape parameter -0.7:

from scipy import stats
x = stats.tukeylambda.rvs(-0.7, loc=2, scale=0.5, size=10000,
                          random_state=1234567) + 1e4

# Now we explore this data with a PPCC plot as well as the related
# probability plot and Box-Cox normplot.  A red line is drawn where we
# expect the PPCC value to be maximal (at the shape parameter -0.7 used
# above):

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
res = stats.ppcc_plot(x, -5, 5, plot=ax)

# We calculate the value where the shape should reach its maximum and a red
# line is drawn there. The line should coincide with the highest point in the
# ppcc_plot.

max = stats.ppcc_max(x)
ax.vlines(max, 0, 1, colors='r', label='Expected shape value')

plt.show()
