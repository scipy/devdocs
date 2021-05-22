# Generate some noisy data:

rng = np.random.default_rng()
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * rng.standard_normal(50)

# Now fit a smoothing cubic spline with a pre-defined internal knots.
# Here we make the knot vector (k+1)-regular by adding boundary knots:

from scipy.interpolate import make_lsq_spline, BSpline
t = [-1, 0, 1]
k = 3
t = np.r_[(x[0],)*(k+1),
          t,
          (x[-1],)*(k+1)]
spl = make_lsq_spline(x, y, t, k)

# For comparison, we also construct an interpolating spline for the same
# set of data:

from scipy.interpolate import make_interp_spline
spl_i = make_interp_spline(x, y)

# Plot both:

import matplotlib.pyplot as plt
xs = np.linspace(-3, 3, 100)
plt.plot(x, y, 'ro', ms=5)
plt.plot(xs, spl(xs), 'g-', lw=3, label='LSQ spline')
plt.plot(xs, spl_i(xs), 'b-', lw=3, alpha=0.7, label='interp spline')
plt.legend(loc='best')
plt.show()

# **NaN handling**: If the input arrays contain ``nan`` values, the result is
# not useful since the underlying spline fitting routines cannot deal with
# ``nan``. A workaround is to use zero weights for not-a-number data points:

y[8] = np.nan
w = np.isnan(y)
y[w] = 0.
tck = make_lsq_spline(x, y, t, w=~w)

# Notice the need to replace a ``nan`` by a numerical value (precise value
# does not matter as long as the corresponding weight is zero.)
