# Plot the function of several orders for real input:

from scipy.special import kv
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 1000)
for N in np.linspace(0, 6, 5):
    plt.plot(x, kv(N, x), label='$K_{{{}}}(x)$'.format(N))
plt.ylim(0, 10)
plt.legend()
plt.title(r'Modified Bessel function of the second kind $K_\nu(x)$')
plt.show()

# Calculate for a single value at multiple orders:

kv([4, 4.5, 5], 1+2j)
# array([ 0.1992+2.3892j,  2.3493+3.6j   ,  7.2827+3.8104j])
