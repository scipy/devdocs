# You can interpolate 1-D points with a B-spline curve.
# Further examples are given in
# :ref:`in the tutorial <tutorial-interpolate_splXXX>`.

import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
x = np.linspace(0, 10, 10)
y = np.sin(x)
spl = splrep(x, y)
x2 = np.linspace(0, 10, 200)
y2 = splev(x2, spl)
plt.plot(x, y, 'o', x2, y2)
plt.show()
