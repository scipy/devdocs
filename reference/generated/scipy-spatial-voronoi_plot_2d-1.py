# Set of point:

import matplotlib.pyplot as plt
rng = np.random.default_rng()
points = rng.random((10,2))

# Voronoi diagram of the points:

from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(points)

# using `voronoi_plot_2d` for visualisation:

fig = voronoi_plot_2d(vor)

# using `voronoi_plot_2d` for visualisation with enhancements:

fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='orange',
                line_width=2, line_alpha=0.6, point_size=2)
plt.show()
