# We can compute integrations of a vector-valued function:

from scipy.integrate import quad_vec
import matplotlib.pyplot as plt
alpha = np.linspace(0.0, 2.0, num=30)
f = lambda x: x**alpha
x0, x1 = 0, 2
y, err = quad_vec(f, x0, x1)
plt.plot(alpha, y)
plt.xlabel(r"$\alpha$")
plt.ylabel(r"$\int_{0}^{2} x^\alpha dx$")
plt.show()
