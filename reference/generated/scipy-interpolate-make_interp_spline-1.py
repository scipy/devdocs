# Use cubic interpolation on Chebyshev nodes:

def cheb_nodes(N):
    jj = 2.*np.arange(N) + 1
    x = np.cos(np.pi * jj / 2 / N)[::-1]
    return x

x = cheb_nodes(20)
y = np.sqrt(1 - x**2)

from scipy.interpolate import BSpline, make_interp_spline
b = make_interp_spline(x, y)
np.allclose(b(x), y)
# True

# Note that the default is a cubic spline with a not-a-knot boundary condition

b.k
# 3

# Here we use a 'natural' spline, with zero 2nd derivatives at edges:

l, r = [(2, 0.0)], [(2, 0.0)]
b_n = make_interp_spline(x, y, bc_type=(l, r))  # or, bc_type="natural"
np.allclose(b_n(x), y)
# True
x0, x1 = x[0], x[-1]
np.allclose([b_n(x0, 2), b_n(x1, 2)], [0, 0])
# True

# Interpolation of parametric curves is also supported. As an example, we
# compute a discretization of a snail curve in polar coordinates

phi = np.linspace(0, 2.*np.pi, 40)
r = 0.3 + np.cos(phi)
x, y = r*np.cos(phi), r*np.sin(phi)  # convert to Cartesian coordinates

# Build an interpolating curve, parameterizing it by the angle

from scipy.interpolate import make_interp_spline
spl = make_interp_spline(phi, np.c_[x, y])

# Evaluate the interpolant on a finer grid (note that we transpose the result
# to unpack it into a pair of x- and y-arrays)

phi_new = np.linspace(0, 2.*np.pi, 100)
x_new, y_new = spl(phi_new).T

# Plot the result

import matplotlib.pyplot as plt
plt.plot(x, y, 'o')
plt.plot(x_new, y_new, '-')
plt.show()
