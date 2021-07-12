import matplotlib.pyplot as plt
from scipy.stats import multivariate_t
x, y = np.mgrid[-1:3:.01, -2:1.5:.01]
pos = np.dstack((x, y))
rv = multivariate_t([1.0, -0.5], [[2.1, 0.3], [0.3, 1.5]], df=2)
fig, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
plt.contourf(x, y, rv.pdf(pos))
