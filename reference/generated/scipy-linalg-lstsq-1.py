from scipy.linalg import lstsq
import matplotlib.pyplot as plt

# Suppose we have the following data:

x = np.array([1, 2.5, 3.5, 4, 5, 7, 8.5])
y = np.array([0.3, 1.1, 1.5, 2.0, 3.2, 6.6, 8.6])

# We want to fit a quadratic polynomial of the form ``y = a + b*x**2``
# to this data.  We first form the "design matrix" M, with a constant
# column of 1s and a column containing ``x**2``:

M = x[:, np.newaxis]**[0, 2]
M
# array([[  1.  ,   1.  ],
# [  1.  ,   6.25],
# [  1.  ,  12.25],
# [  1.  ,  16.  ],
# [  1.  ,  25.  ],
# [  1.  ,  49.  ],
# [  1.  ,  72.25]])

# We want to find the least-squares solution to ``M.dot(p) = y``,
# where ``p`` is a vector with length 2 that holds the parameters
# ``a`` and ``b``.

p, res, rnk, s = lstsq(M, y)
p
# array([ 0.20925829,  0.12013861])

# Plot the data and the fitted curve.

plt.plot(x, y, 'o', label='data')
xx = np.linspace(0, 9, 101)
yy = p[0] + p[1]*xx**2
plt.plot(xx, yy, label='least squares fit, $y = a + bx^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(framealpha=1, shadow=True)
plt.grid(alpha=0.25)
plt.show()
