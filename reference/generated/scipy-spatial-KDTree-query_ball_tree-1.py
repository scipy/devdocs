# You can search all pairs of points between two kd-trees within a distance:

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import KDTree
rng = np.random.default_rng()
points1 = rng.random((15, 2))
points2 = rng.random((15, 2))
plt.figure(figsize=(6, 6))
plt.plot(points1[:, 0], points1[:, 1], "xk", markersize=14)
plt.plot(points2[:, 0], points2[:, 1], "og", markersize=14)
kd_tree1 = KDTree(points1)
kd_tree2 = KDTree(points2)
indexes = kd_tree1.query_ball_tree(kd_tree2, r=0.2)
for i in range(len(indexes)):
    for j in indexes[i]:
        plt.plot([points1[i, 0], points2[j, 0]],
            [points1[i, 1], points2[j, 1]], "-r")
plt.show()
