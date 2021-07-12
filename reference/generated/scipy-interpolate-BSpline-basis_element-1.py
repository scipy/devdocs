# Construct a cubic B-spline:

from scipy.interpolate import BSpline
b = BSpline.basis_element([0, 1, 2, 3, 4])
k = b.k
b.t[k:-k]
# array([ 0.,  1.,  2.,  3.,  4.])
k
# 3

# Construct a quadratic B-spline on ``[0, 1, 1, 2]``, and compare
# to its explicit form:

t = [-1, 0, 1, 1, 2]
b = BSpline.basis_element(t[1:])
def f(x):
    return np.where(x < 1, x*x, (2. - x)**2)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x = np.linspace(0, 2, 51)
ax.plot(x, b(x), 'g', lw=3)
ax.plot(x, f(x), 'r', lw=8, alpha=0.4)
ax.grid(True)
plt.show()
