from scipy import special
import matplotlib.pyplot as plt

x = np.linspace(-3, 3)
z = special.wofz(x)

plt.plot(x, z.real, label='wofz(x).real')
plt.plot(x, z.imag, label='wofz(x).imag')
plt.xlabel('$x$')
plt.legend(framealpha=1, shadow=True)
plt.grid(alpha=0.25)
plt.show()
