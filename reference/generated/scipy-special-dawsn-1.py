from scipy import special
import matplotlib.pyplot as plt
x = np.linspace(-15, 15, num=1000)
plt.plot(x, special.dawsn(x))
plt.xlabel('$x$')
plt.ylabel('$dawsn(x)$')
plt.show()
