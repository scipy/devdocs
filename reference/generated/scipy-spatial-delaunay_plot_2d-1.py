import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, delaunay_plot_2d

# The Delaunay triangulation of a set of random points:

rng = np.random.default_rng()
points = rng.random((30, 2))
tri = Delaunay(points)

# Plot it:

_ = delaunay_plot_2d(tri)
plt.show()
