from scipy import special
import matplotlib.pyplot as plt
x = np.linspace(-3, 3)
plt.plot(x, special.erfi(x))
plt.xlabel('$x$')
plt.ylabel('$erfi(x)$')
plt.show()
