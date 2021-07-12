from scipy import special
import matplotlib.pyplot as plt
x = np.linspace(-3, 3)
plt.plot(x, special.erfcx(x))
plt.xlabel('$x$')
plt.ylabel('$erfcx(x)$')
plt.show()
