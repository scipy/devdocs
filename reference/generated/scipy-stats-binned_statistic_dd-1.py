from scipy import stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Take an array of 600 (x, y) coordinates as an example.
# `binned_statistic_dd` can handle arrays of higher dimension `D`. But a plot
# of dimension `D+1` is required.

mu = np.array([0., 1.])
sigma = np.array([[1., -0.5],[-0.5, 1.5]])
multinormal = stats.multivariate_normal(mu, sigma)
data = multinormal.rvs(size=600, random_state=235412)
data.shape
# (600, 2)

# Create bins and count how many arrays fall in each bin:

N = 60
x = np.linspace(-3, 3, N)
y = np.linspace(-3, 4, N)
ret = stats.binned_statistic_dd(data, np.arange(600), bins=[x, y],
                                statistic='count')
bincounts = ret.statistic

# Set the volume and the location of bars:

dx = x[1] - x[0]
dy = y[1] - y[0]
x, y = np.meshgrid(x[:-1]+dx/2, y[:-1]+dy/2)
z = 0

bincounts = bincounts.ravel()
x = x.ravel()
y = y.ravel()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
with np.errstate(divide='ignore'):   # silence random axes3d warning
    ax.bar3d(x, y, z, dx, dy, bincounts)

# Reuse bin numbers and bin edges with new values:

ret2 = stats.binned_statistic_dd(data, -np.arange(600),
                                 binned_statistic_result=ret,
                                 statistic='mean')
