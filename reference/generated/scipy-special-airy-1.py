# Compute the Airy functions on the interval [-15, 5].

from scipy import special
x = np.linspace(-15, 5, 201)
ai, aip, bi, bip = special.airy(x)

# Plot Ai(x) and Bi(x).

import matplotlib.pyplot as plt
plt.plot(x, ai, 'r', label='Ai(x)')
plt.plot(x, bi, 'b--', label='Bi(x)')
plt.ylim(-0.5, 1.0)
plt.grid()
plt.legend(loc='upper left')
plt.show()
