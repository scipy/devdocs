import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt

def mandala(n_iter, n_points, radius):
    """Creates a mandala figure using Voronoi tesselations.
# ...
    Parameters
    ----------
    n_iter : int
        Number of iterations, i.e. how many times the equidistant points will
        be generated.
    n_points : int
        Number of points to draw per iteration.
    radius : scalar
        The radial expansion factor.
# ...
    Returns
    -------
    fig : matplotlib.Figure instance
# ...
    Notes
    -----
    This code is adapted from the work of Audrey Roy Greenfeld [1]_ and Carlos
    Focil-Espinosa [2]_, who created beautiful mandalas with Python code.  That
    code in turn was based on Antonio Sánchez Chinchón's R code [3]_.
# ...
    References
    ----------
    .. [1] https://www.codemakesmehappy.com/2019/09/voronoi-mandalas.html
# ...
    .. [2] https://github.com/CarlosFocil/mandalapy
# ...
    .. [3] https://github.com/aschinchon/mandalas
# ...
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    ax.set_aspect('equal', adjustable='box')
# ...
    angles = np.linspace(0, 2*np.pi * (1 - 1/n_points), num=n_points) + np.pi/2
    # Starting from a single center point, add points iteratively
    xy = np.array([[0, 0]])
    for k in range(n_iter):
        t1 = np.array([])
        t2 = np.array([])
        # Add `n_points` new points around each existing point in this iteration
        for i in range(xy.shape[0]):
            t1 = np.append(t1, xy[i, 0] + radius**k * np.cos(angles))
            t2 = np.append(t2, xy[i, 1] + radius**k * np.sin(angles))
# ...
        xy = np.column_stack((t1, t2))
# ...
    # Create the Mandala figure via a Voronoi plot
    spatial.voronoi_plot_2d(spatial.Voronoi(xy), ax=ax)
# ...
    return fig

# Modify the following parameters in order to get different figures
n_iter = 3
n_points = 6
radius = 4

fig = mandala(n_iter, n_points, radius)
plt.show()
