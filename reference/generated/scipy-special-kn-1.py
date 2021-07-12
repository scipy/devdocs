# Plot the function of several orders for real input:

from scipy.special import kn
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 1000)
for N in range(6):
    plt.plot(x, kn(N, x), label='$K_{}(x)$'.format(N))
plt.ylim(0, 10)
plt.legend()
plt.title(r'Modified Bessel function of the second kind $K_n(x)$')
plt.show()

# Calculate for a single value at multiple orders:

kn([4, 5, 6], 1)
# array([   44.23241585,   360.9605896 ,  3653.83831186])
