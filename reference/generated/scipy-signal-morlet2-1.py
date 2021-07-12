from scipy import signal
import matplotlib.pyplot as plt

M = 100
s = 4.0
w = 2.0
wavelet = signal.morlet2(M, s, w)
plt.plot(abs(wavelet))
plt.show()

# This example shows basic use of `morlet2` with `cwt` in time-frequency
# analysis:

from scipy import signal
import matplotlib.pyplot as plt
t, dt = np.linspace(0, 1, 200, retstep=True)
fs = 1/dt
w = 6.
sig = np.cos(2*np.pi*(50 + 10*t)*t) + np.sin(40*np.pi*t)
freq = np.linspace(1, fs/2, 100)
widths = w*fs / (2*freq*np.pi)
cwtm = signal.cwt(sig, signal.morlet2, widths, w=w)
plt.pcolormesh(t, freq, np.abs(cwtm), cmap='viridis', shading='gouraud')
plt.show()
