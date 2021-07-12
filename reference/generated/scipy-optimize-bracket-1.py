# This function can find a downward convex region of a function:

import matplotlib.pyplot as plt
from scipy.optimize import bracket
def f(x):
    return 10*x**2 + 3*x + 5
x = np.linspace(-2, 2)
y = f(x)
init_xa, init_xb = 0, 1
xa, xb, xc, fa, fb, fc, funcalls = bracket(f, xa=init_xa, xb=init_xb)
plt.axvline(x=init_xa, color="k", linestyle="--")
plt.axvline(x=init_xb, color="k", linestyle="--")
plt.plot(x, y, "-k")
plt.plot(xa, fa, "bx")
plt.plot(xb, fb, "rx")
plt.plot(xc, fc, "bx")
plt.show()
