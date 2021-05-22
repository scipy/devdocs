from scipy.special import eval_legendre

# Evaluate the zero-order Legendre polynomial at x = 0

eval_legendre(0, 0)
# 1.0

# Evaluate the first-order Legendre polynomial between -1 and 1

X = np.linspace(-1, 1, 5)  # Domain of Legendre polynomials
eval_legendre(1, X)
# array([-1. , -0.5,  0. ,  0.5,  1. ])

# Evaluate Legendre polynomials of order 0 through 4 at x = 0

N = range(0, 5)
eval_legendre(N, 0)
# array([ 1.   ,  0.   , -0.5  ,  0.   ,  0.375])

# Plot Legendre polynomials of order 0 through 4

X = np.linspace(-1, 1)

import matplotlib.pyplot as plt
for n in range(0, 5):
    y = eval_legendre(n, X)
    plt.plot(X, y, label=r'$P_{}(x)$'.format(n))

plt.title("Legendre Polynomials")
plt.xlabel("x")
plt.ylabel(r'$P_n(x)$')
plt.legend(loc='lower right')
plt.show()
