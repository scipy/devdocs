from scipy import signal
import matplotlib.pyplot as plt

sys = signal.TransferFunction([1], [1, 1])
w, mag, phase = sys.bode()

plt.figure()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase)  # Bode phase plot
plt.show()
