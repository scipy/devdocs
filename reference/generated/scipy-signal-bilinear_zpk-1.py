from scipy import signal
import matplotlib.pyplot as plt

fs = 100
bf = 2 * np.pi * np.array([7, 13])
filts = signal.lti(*signal.butter(4, bf, btype='bandpass', analog=True,
                                  output='zpk'))
filtz = signal.lti(*signal.bilinear_zpk(filts.zeros, filts.poles,
                                        filts.gain, fs))
wz, hz = signal.freqz_zpk(filtz.zeros, filtz.poles, filtz.gain)
ws, hs = signal.freqs_zpk(filts.zeros, filts.poles, filts.gain,
                          worN=fs*wz)
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(hz).clip(1e-15)),
             label=r'$|H_z(e^{j \omega})|$')
plt.semilogx(wz*fs/(2*np.pi), 20*np.log10(np.abs(hs).clip(1e-15)),
             label=r'$|H(j \omega)|$')
plt.legend()
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid()
