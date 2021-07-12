# MLS uses binary convention:

from scipy.signal import max_len_seq
max_len_seq(4)[0]
# array([1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0], dtype=int8)

# MLS has a white spectrum (except for DC):

import matplotlib.pyplot as plt
from numpy.fft import fft, ifft, fftshift, fftfreq
seq = max_len_seq(6)[0]*2-1  # +1 and -1
spec = fft(seq)
N = len(seq)
plt.plot(fftshift(fftfreq(N)), fftshift(np.abs(spec)), '.-')
plt.margins(0.1, 0.1)
plt.grid(True)
plt.show()

# Circular autocorrelation of MLS is an impulse:

acorrcirc = ifft(spec * np.conj(spec)).real
plt.figure()
plt.plot(np.arange(-N/2+1, N/2+1), fftshift(acorrcirc), '.-')
plt.margins(0.1, 0.1)
plt.grid(True)
plt.show()

# Linear autocorrelation of MLS is approximately an impulse:

acorr = np.correlate(seq, seq, 'full')
plt.figure()
plt.plot(np.arange(-N+1, N), acorr, '.-')
plt.margins(0.1, 0.1)
plt.grid(True)
plt.show()
