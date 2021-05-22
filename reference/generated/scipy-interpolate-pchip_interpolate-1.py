# We can interpolate 2D observed data using pchip interpolation:

import matplotlib.pyplot as plt
from scipy.interpolate import pchip_interpolate
x_observed = np.linspace(0.0, 10.0, 11)
y_observed = np.sin(x_observed)
x = np.linspace(min(x_observed), max(x_observed), num=100)
y = pchip_interpolate(x_observed, y_observed, x)
plt.plot(x_observed, y_observed, "o", label="observation")
plt.plot(x, y, label="pchip interpolation")
plt.legend()
plt.show()
