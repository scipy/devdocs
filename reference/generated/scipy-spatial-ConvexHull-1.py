# Convex hull of a random set of points:

from scipy.spatial import ConvexHull, convex_hull_plot_2d
rng = np.random.default_rng()
points = rng.random((30, 2))   # 30 random points in 2-D
hull = ConvexHull(points)

# Plot it:

import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

# We could also have directly used the vertices of the hull, which
# for 2-D are guaranteed to be in counterclockwise order:

plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
plt.show()

# Facets visible from a point:

# Create a square and add a point above the square.

generators = np.array([[0.2, 0.2],
                       [0.2, 0.4],
                       [0.4, 0.4],
                       [0.4, 0.2],
                       [0.3, 0.6]])

# Call ConvexHull with the QG option. QG4 means
# compute the portions of the hull not including
# point 4, indicating the facets that are visible
# from point 4.

hull = ConvexHull(points=generators,
                  qhull_options='QG4')

# The "good" array indicates which facets are
# visible from point 4.

print(hull.simplices)
# [[1 0]
# [1 2]
# [3 0]
# [3 2]]
print(hull.good)
# [False  True False False]

# Now plot it, highlighting the visible facets.

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for visible_facet in hull.simplices[hull.good]:
    ax.plot(hull.points[visible_facet, 0],
            hull.points[visible_facet, 1],
            color='violet',
            lw=6)
convex_hull_plot_2d(hull, ax=ax)
# <Figure size 640x480 with 1 Axes> # may vary
plt.show()
