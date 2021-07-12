# Generate a discretization of a limacon curve in the polar coordinates:

phi = np.linspace(0, 2.*np.pi, 40)
r = 0.5 + np.cos(phi)         # polar coords
x, y = r * np.cos(phi), r * np.sin(phi)    # convert to cartesian

# And interpolate:

from scipy.interpolate import splprep, splev
tck, u = splprep([x, y], s=0)
new_points = splev(u, tck)

# Notice that (i) we force interpolation by using `s=0`,
# (ii) the parameterization, ``u``, is generated automatically.
# Now plot the result:

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x, y, 'ro')
ax.plot(new_points[0], new_points[1], 'r-')
plt.show()
