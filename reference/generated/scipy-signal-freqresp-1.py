# Generating the Nyquist plot of a transfer function

from scipy import signal
import matplotlib.pyplot as plt

# Construct the transfer function :math:`H(s) = \frac{5}{(s-1)^3}`:

s1 = signal.ZerosPolesGain([], [1, 1, 1], [5])

w, H = signal.freqresp(s1)

plt.figure()
plt.plot(H.real, H.imag, "b")
plt.plot(H.real, -H.imag, "r")
plt.show()
