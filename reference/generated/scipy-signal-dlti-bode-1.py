from scipy import signal
import matplotlib.pyplot as plt

# Construct the transfer function :math:`H(z) = \frac{1}{z^2 + 2z + 3}`
# with sampling time 0.5s:

sys = signal.TransferFunction([1], [1, 2, 3], dt=0.5)

# Equivalent: signal.dbode(sys)

w, mag, phase = sys.bode()

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()
