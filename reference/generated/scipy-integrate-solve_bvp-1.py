# In the first example, we solve Bratu's problem::

# y'' + k * exp(y) = 0
# y(0) = y(1) = 0

# for k = 1.

# We rewrite the equation as a first-order system and implement its
# right-hand side evaluation::

# y1' = y2
# y2' = -exp(y1)

def fun(x, y):
    return np.vstack((y[1], -np.exp(y[0])))

# Implement evaluation of the boundary condition residuals:

def bc(ya, yb):
    return np.array([ya[0], yb[0]])

# Define the initial mesh with 5 nodes:

x = np.linspace(0, 1, 5)

# This problem is known to have two solutions. To obtain both of them, we
# use two different initial guesses for y. We denote them by subscripts
# a and b.

y_a = np.zeros((2, x.size))
y_b = np.zeros((2, x.size))
y_b[0] = 3

# Now we are ready to run the solver.

from scipy.integrate import solve_bvp
res_a = solve_bvp(fun, bc, x, y_a)
res_b = solve_bvp(fun, bc, x, y_b)

# Let's plot the two found solutions. We take an advantage of having the
# solution in a spline form to produce a smooth plot.

x_plot = np.linspace(0, 1, 100)
y_plot_a = res_a.sol(x_plot)[0]
y_plot_b = res_b.sol(x_plot)[0]
import matplotlib.pyplot as plt
plt.plot(x_plot, y_plot_a, label='y_a')
plt.plot(x_plot, y_plot_b, label='y_b')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# We see that the two solutions have similar shape, but differ in scale
# significantly.

# In the second example, we solve a simple Sturm-Liouville problem::

# y'' + k**2 * y = 0
# y(0) = y(1) = 0

# It is known that a non-trivial solution y = A * sin(k * x) is possible for
# k = pi * n, where n is an integer. To establish the normalization constant
# A = 1 we add a boundary condition::

# y'(0) = k

# Again, we rewrite our equation as a first-order system and implement its
# right-hand side evaluation::

# y1' = y2
# y2' = -k**2 * y1

def fun(x, y, p):
    k = p[0]
    return np.vstack((y[1], -k**2 * y[0]))

# Note that parameters p are passed as a vector (with one element in our
# case).

# Implement the boundary conditions:

def bc(ya, yb, p):
    k = p[0]
    return np.array([ya[0], yb[0], ya[1] - k])

# Set up the initial mesh and guess for y. We aim to find the solution for
# k = 2 * pi, to achieve that we set values of y to approximately follow
# sin(2 * pi * x):

x = np.linspace(0, 1, 5)
y = np.zeros((2, x.size))
y[0, 1] = 1
y[0, 3] = -1

# Run the solver with 6 as an initial guess for k.

sol = solve_bvp(fun, bc, x, y, p=[6])

# We see that the found k is approximately correct:

sol.p[0]
# 6.28329460046

# And, finally, plot the solution to see the anticipated sinusoid:

x_plot = np.linspace(0, 1, 100)
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
