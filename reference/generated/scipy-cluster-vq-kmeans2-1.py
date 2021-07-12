from scipy.cluster.vq import kmeans2
import matplotlib.pyplot as plt

# Create z, an array with shape (100, 2) containing a mixture of samples
# from three multivariate normal distributions.

rng = np.random.default_rng()
a = rng.multivariate_normal([0, 6], [[2, 1], [1, 1.5]], size=45)
b = rng.multivariate_normal([2, 0], [[1, -1], [-1, 3]], size=30)
c = rng.multivariate_normal([6, 4], [[5, 0], [0, 1.2]], size=25)
z = np.concatenate((a, b, c))
rng.shuffle(z)

# Compute three clusters.

centroid, label = kmeans2(z, 3, minit='points')
centroid
# array([[ 2.22274463, -0.61666946],  # may vary
# [ 0.54069047,  5.86541444],
# [ 6.73846769,  4.01991898]])

# How many points are in each cluster?

counts = np.bincount(label)
counts
# array([29, 51, 20])  # may vary

# Plot the clusters.

w0 = z[label == 0]
w1 = z[label == 1]
w2 = z[label == 2]
plt.plot(w0[:, 0], w0[:, 1], 'o', alpha=0.5, label='cluster 0')
plt.plot(w1[:, 0], w1[:, 1], 'd', alpha=0.5, label='cluster 1')
plt.plot(w2[:, 0], w2[:, 1], 's', alpha=0.5, label='cluster 2')
plt.plot(centroid[:, 0], centroid[:, 1], 'k*', label='centroids')
plt.axis('equal')
plt.legend(shadow=True)
plt.show()
