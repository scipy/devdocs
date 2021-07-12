from scipy import stats
import matplotlib.pyplot as plt

# Generate some data and determine optimal ``lmbda``

rng = np.random.default_rng()
x = stats.loggamma.rvs(5, size=30, random_state=rng) + 5
lmax = stats.yeojohnson_normmax(x)

fig = plt.figure()
ax = fig.add_subplot(111)
prob = stats.yeojohnson_normplot(x, -10, 10, plot=ax)
ax.axvline(lmax, color='r')

plt.show()
