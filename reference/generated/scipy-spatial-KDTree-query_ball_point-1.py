from scipy import spatial
x, y = np.mgrid[0:5, 0:5]
points = np.c_[x.ravel(), y.ravel()]
tree = spatial.KDTree(points)
sorted(tree.query_ball_point([2, 0], 1))
# [5, 10, 11, 15]

# Query multiple points and plot the results:

import matplotlib.pyplot as plt
points = np.asarray(points)
plt.plot(points[:,0], points[:,1], '.')
for results in tree.query_ball_point(([2, 0], [3, 3]), 1):
    nearby_points = points[results]
    plt.plot(nearby_points[:,0], nearby_points[:,1], 'o')
plt.margins(0.1, 0.1)
plt.show()
