from scipy import stats
import matplotlib.pyplot as plt

# Generate some non-normally distributed data, and create a Yeo-Johnson plot:

x = stats.loggamma.rvs(5, size=500) + 5
fig = plt.figure()
ax = fig.add_subplot(111)
prob = stats.yeojohnson_normplot(x, -20, 20, plot=ax)

# Determine and plot the optimal ``lmbda`` to transform ``x`` and plot it in
# the same plot:

_, maxlog = stats.yeojohnson(x)
ax.axvline(maxlog, color='r')

plt.show()
