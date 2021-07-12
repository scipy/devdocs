# Triangulation of a set of points:

points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
from scipy.spatial import Delaunay
tri = Delaunay(points)

# We can plot it:

import matplotlib.pyplot as plt
plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.plot(points[:,0], points[:,1], 'o')
plt.show()

# Point indices and coordinates for the two triangles forming the
# triangulation:

tri.simplices
# array([[2, 3, 0],                 # may vary
# [3, 1, 0]], dtype=int32)

# Note that depending on how rounding errors go, the simplices may
# be in a different order than above.

points[tri.simplices]
# array([[[ 1. ,  0. ],            # may vary
# [ 1. ,  1. ],
# [ 0. ,  0. ]],
# [[ 1. ,  1. ],
# [ 0. ,  1.1],
# [ 0. ,  0. ]]])

# Triangle 0 is the only neighbor of triangle 1, and it's opposite to
# vertex 1 of triangle 1:

tri.neighbors[1]
# array([-1,  0, -1], dtype=int32)
points[tri.simplices[1,1]]
# array([ 0. ,  1.1])

# We can find out which triangle points are in:

p = np.array([(0.1, 0.2), (1.5, 0.5), (0.5, 1.05)])
tri.find_simplex(p)
# array([ 1, -1, 1], dtype=int32)

# The returned integers in the array are the indices of the simplex the
# corresponding point is in. If -1 is returned, the point is in no simplex.
# Be aware that the shortcut in the following example only works corretcly
# for valid points as invalid points result in -1 which is itself a valid
# index for the last simplex in the list.

p_valids = np.array([(0.1, 0.2), (0.5, 1.05)])
tri.simplices[tri.find_simplex(p_valids)]
# array([[3, 1, 0],                 # may vary
# [3, 1, 0]], dtype=int32)

# We can also compute barycentric coordinates in triangle 1 for
# these points:

b = tri.transform[1,:2].dot(np.transpose(p - tri.transform[1,2]))
np.c_[np.transpose(b), 1 - b.sum(axis=0)]
# array([[ 0.1       ,  0.09090909,  0.80909091],
# [ 1.5       , -0.90909091,  0.40909091],
# [ 0.5       ,  0.5       ,  0.        ]])

# The coordinates for the first point are all positive, meaning it
# is indeed inside the triangle. The third point is on a vertex,
# hence its null third coordinate.
