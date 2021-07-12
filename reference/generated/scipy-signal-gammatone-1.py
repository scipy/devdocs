# 16-sample 4th order FIR Gammatone filter centered at 440 Hz

from scipy import signal
signal.gammatone(440, 'fir', numtaps=16, fs=16000)
# (array([ 0.00000000e+00,  2.22196719e-07,  1.64942101e-06,  4.99298227e-06,
# 1.01993969e-05,  1.63125770e-05,  2.14648940e-05,  2.29947263e-05,
# 1.76776931e-05,  2.04980537e-06, -2.72062858e-05, -7.28455299e-05,
# -1.36651076e-04, -2.19066855e-04, -3.18905076e-04, -4.33156712e-04]),
# [1.0])

# IIR Gammatone filter centered at 440 Hz

from scipy import signal
import matplotlib.pyplot as plt

b, a = signal.gammatone(440, 'iir', fs=16000)
w, h = signal.freqz(b, a)
plt.plot(w / ((2 * np.pi) / 16000), 20 * np.log10(abs(h)))
plt.xscale('log')
plt.title('Gammatone filter frequency response')
plt.xlabel('Frequency')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(440, color='green') # cutoff frequency
plt.show()
