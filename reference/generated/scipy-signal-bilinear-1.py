from scipy import signal
import matplotlib.pyplot as plt

fs = 100
bf = 2 * np.pi * np.array([7, 13])
filts = signal.lti(*signal.butter(4, bf, btype='bandpass',
                                  analog=True))
filtz = signal.lti(*signal.bilinear(filts.num, filts.den, fs))
wz, hz = signal.freqz(filtz.num, filtz.den)
ws, hs = signal.freqs(filts.num, filts.den, worN=fs*wz)

plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(hz).clip(1e-15)),
             label=r'$|H_z(e^{j \omega})|$')
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(hs).clip(1e-15)),
             label=r'$|H(j \omega)|$')
plt.legend()
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid()
