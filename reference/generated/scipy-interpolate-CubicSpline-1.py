# In this example the cubic spline is used to interpolate a sampled sinusoid.
# You can see that the spline continuity property holds for the first and
# second derivatives and violates only for the third derivative.

from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
x = np.arange(10)
y = np.sin(x)
cs = CubicSpline(x, y)
xs = np.arange(-0.5, 9.6, 0.1)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='data')
ax.plot(xs, np.sin(xs), label='true')
ax.plot(xs, cs(xs), label="S")
ax.plot(xs, cs(xs, 1), label="S'")
ax.plot(xs, cs(xs, 2), label="S''")
ax.plot(xs, cs(xs, 3), label="S'''")
ax.set_xlim(-0.5, 9.5)
ax.legend(loc='lower left', ncol=2)
plt.show()

# In the second example, the unit circle is interpolated with a spline. A
# periodic boundary condition is used. You can see that the first derivative
# values, ds/dx=0, ds/dy=1 at the periodic point (1, 0) are correctly
# computed. Note that a circle cannot be exactly represented by a cubic
# spline. To increase precision, more breakpoints would be required.

theta = 2 * np.pi * np.linspace(0, 1, 5)
y = np.c_[np.cos(theta), np.sin(theta)]
cs = CubicSpline(theta, y, bc_type='periodic')
print("ds/dx={:.1f} ds/dy={:.1f}".format(cs(0, 1)[0], cs(0, 1)[1]))
# ds/dx=0.0 ds/dy=1.0
xs = 2 * np.pi * np.linspace(0, 1, 100)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(y[:, 0], y[:, 1], 'o', label='data')
ax.plot(np.cos(xs), np.sin(xs), label='true')
ax.plot(cs(xs)[:, 0], cs(xs)[:, 1], label='spline')
ax.axes.set_aspect('equal')
ax.legend(loc='center')
plt.show()

# The third example is the interpolation of a polynomial y = x**3 on the
# interval 0 <= x<= 1. A cubic spline can represent this function exactly.
# To achieve that we need to specify values and first derivatives at
# endpoints of the interval. Note that y' = 3 * x**2 and thus y'(0) = 0 and
# y'(1) = 3.

cs = CubicSpline([0, 1], [0, 1], bc_type=((1, 0), (1, 3)))
x = np.linspace(0, 1)
np.allclose(x**3, cs(x))
# True
