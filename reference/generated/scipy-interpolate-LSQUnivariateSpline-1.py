from scipy.interpolate import LSQUnivariateSpline, UnivariateSpline
import matplotlib.pyplot as plt
rng = np.random.default_rng()
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * rng.standard_normal(50)

# Fit a smoothing spline with a pre-defined internal knots:

t = [-1, 0, 1]
spl = LSQUnivariateSpline(x, y, t)

xs = np.linspace(-3, 3, 1000)
plt.plot(x, y, 'ro', ms=5)
plt.plot(xs, spl(xs), 'g-', lw=3)
plt.show()

# Check the knot vector:

spl.get_knots()
# array([-3., -1., 0., 1., 3.])

# Constructing lsq spline using the knots from another spline:

x = np.arange(10)
s = UnivariateSpline(x, x, s=0)
s.get_knots()
# array([ 0.,  2.,  3.,  4.,  5.,  6.,  7.,  9.])
knt = s.get_knots()
s1 = LSQUnivariateSpline(x, x, knt[1:-1])    # Chop 1st and last knot
s1.get_knots()
# array([ 0.,  2.,  3.,  4.,  5.,  6.,  7.,  9.])
