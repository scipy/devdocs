# In this example we find a minimum of the Rosenbrock function without bounds
# on independent variables.

def fun_rosenbrock(x):
    return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])

# Notice that we only provide the vector of the residuals. The algorithm
# constructs the cost function as a sum of squares of the residuals, which
# gives the Rosenbrock function. The exact minimum is at ``x = [1.0, 1.0]``.

from scipy.optimize import least_squares
x0_rosenbrock = np.array([2, 2])
res_1 = least_squares(fun_rosenbrock, x0_rosenbrock)
res_1.x
# array([ 1.,  1.])
res_1.cost
# 9.8669242910846867e-30
res_1.optimality
# 8.8928864934219529e-14

# We now constrain the variables, in such a way that the previous solution
# becomes infeasible. Specifically, we require that ``x[1] >= 1.5``, and
# ``x[0]`` left unconstrained. To this end, we specify the `bounds` parameter
# to `least_squares` in the form ``bounds=([-np.inf, 1.5], np.inf)``.

# We also provide the analytic Jacobian:

def jac_rosenbrock(x):
    return np.array([
        [-20 * x[0], 10],
        [-1, 0]])

# Putting this all together, we see that the new solution lies on the bound:

res_2 = least_squares(fun_rosenbrock, x0_rosenbrock, jac_rosenbrock,
                      bounds=([-np.inf, 1.5], np.inf))
res_2.x
# array([ 1.22437075,  1.5       ])
res_2.cost
# 0.025213093946805685
res_2.optimality
# 1.5885401433157753e-07

# Now we solve a system of equations (i.e., the cost function should be zero
# at a minimum) for a Broyden tridiagonal vector-valued function of 100000
# variables:

def fun_broyden(x):
    f = (3 - x) * x + 1
    f[1:] -= x[:-1]
    f[:-1] -= 2 * x[1:]
    return f

# The corresponding Jacobian matrix is sparse. We tell the algorithm to
# estimate it by finite differences and provide the sparsity structure of
# Jacobian to significantly speed up this process.

from scipy.sparse import lil_matrix
def sparsity_broyden(n):
    sparsity = lil_matrix((n, n), dtype=int)
    i = np.arange(n)
    sparsity[i, i] = 1
    i = np.arange(1, n)
    sparsity[i, i - 1] = 1
    i = np.arange(n - 1)
    sparsity[i, i + 1] = 1
    return sparsity
# ...
n = 100000
x0_broyden = -np.ones(n)
# ...
res_3 = least_squares(fun_broyden, x0_broyden,
                      jac_sparsity=sparsity_broyden(n))
res_3.cost
# 4.5687069299604613e-23
res_3.optimality
# 1.1650454296851518e-11

# Let's also solve a curve fitting problem using robust loss function to
# take care of outliers in the data. Define the model function as
# ``y = a + b * exp(c * t)``, where t is a predictor variable, y is an
# observation and a, b, c are parameters to estimate.

# First, define the function which generates the data with noise and
# outliers, define the model parameters, and generate data:

from numpy.random import default_rng
rng = default_rng()
def gen_data(t, a, b, c, noise=0., n_outliers=0, seed=None):
    rng = default_rng(seed)
# ...
    y = a + b * np.exp(t * c)
# ...
    error = noise * rng.standard_normal(t.size)
    outliers = rng.integers(0, t.size, n_outliers)
    error[outliers] *= 10
# ...
    return y + error
# ...
a = 0.5
b = 2.0
c = -1
t_min = 0
t_max = 10
n_points = 15
# ...
t_train = np.linspace(t_min, t_max, n_points)
y_train = gen_data(t_train, a, b, c, noise=0.1, n_outliers=3)

# Define function for computing residuals and initial estimate of
# parameters.

def fun(x, t, y):
    return x[0] + x[1] * np.exp(x[2] * t) - y
# ...
x0 = np.array([1.0, 1.0, 0.0])

# Compute a standard least-squares solution:

res_lsq = least_squares(fun, x0, args=(t_train, y_train))

# Now compute two solutions with two different robust loss functions. The
# parameter `f_scale` is set to 0.1, meaning that inlier residuals should
# not significantly exceed 0.1 (the noise level used).

res_soft_l1 = least_squares(fun, x0, loss='soft_l1', f_scale=0.1,
                            args=(t_train, y_train))
res_log = least_squares(fun, x0, loss='cauchy', f_scale=0.1,
                        args=(t_train, y_train))

# And, finally, plot all the curves. We see that by selecting an appropriate
# `loss`  we can get estimates close to optimal even in the presence of
# strong outliers. But keep in mind that generally it is recommended to try
# 'soft_l1' or 'huber' losses first (if at all necessary) as the other two
# options may cause difficulties in optimization process.

t_test = np.linspace(t_min, t_max, n_points * 10)
y_true = gen_data(t_test, a, b, c)
y_lsq = gen_data(t_test, *res_lsq.x)
y_soft_l1 = gen_data(t_test, *res_soft_l1.x)
y_log = gen_data(t_test, *res_log.x)
# ...
import matplotlib.pyplot as plt
plt.plot(t_train, y_train, 'o')
plt.plot(t_test, y_true, 'k', linewidth=2, label='true')
plt.plot(t_test, y_lsq, label='linear loss')
plt.plot(t_test, y_soft_l1, label='soft_l1 loss')
plt.plot(t_test, y_log, label='cauchy loss')
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()

# In the next example, we show how complex-valued residual functions of
# complex variables can be optimized with ``least_squares()``. Consider the
# following function:

def f(z):
    return z - (0.5 + 0.5j)

# We wrap it into a function of real variables that returns real residuals
# by simply handling the real and imaginary parts as independent variables:

def f_wrap(x):
    fx = f(x[0] + 1j*x[1])
    return np.array([fx.real, fx.imag])

# Thus, instead of the original m-D complex function of n complex
# variables we optimize a 2m-D real function of 2n real variables:

from scipy.optimize import least_squares
res_wrapped = least_squares(f_wrap, (0.1, 0.1), bounds=([0, 0], [1, 1]))
z = res_wrapped.x[0] + res_wrapped.x[1]*1j
z
# (0.49999999999925893+0.49999999999925893j)
