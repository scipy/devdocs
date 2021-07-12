from scipy.spatial import ConvexHull
rng = np.random.default_rng()
points = rng.random((30, 2))   # 30 random points in 2-D
hull = ConvexHull(points)

# The convex hull is represented as a set of N 1-D simplices,
# which in 2-D means line segments. The storage scheme is exactly the
# same as for the simplices in the Delaunay triangulation discussed
# above.

# We can illustrate the above result:

import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()
