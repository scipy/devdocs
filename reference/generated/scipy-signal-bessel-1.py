# Plot the phase-normalized frequency response, showing the relationship
# to the Butterworth's cutoff frequency (green):

from scipy import signal
import matplotlib.pyplot as plt

b, a = signal.butter(4, 100, 'low', analog=True)
w, h = signal.freqs(b, a)
plt.semilogx(w, 20 * np.log10(np.abs(h)), color='silver', ls='dashed')
b, a = signal.bessel(4, 100, 'low', analog=True, norm='phase')
w, h = signal.freqs(b, a)
plt.semilogx(w, 20 * np.log10(np.abs(h)))
plt.title('Bessel filter magnitude response (with Butterworth)')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='green')  # cutoff frequency
plt.show()

# and the phase midpoint:

plt.figure()
plt.semilogx(w, np.unwrap(np.angle(h)))
plt.axvline(100, color='green')  # cutoff frequency
plt.axhline(-np.pi, color='red')  # phase midpoint
plt.title('Bessel filter phase response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Phase [radians]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.show()

# Plot the magnitude-normalized frequency response, showing the -3 dB cutoff:

b, a = signal.bessel(3, 10, 'low', analog=True, norm='mag')
w, h = signal.freqs(b, a)
plt.semilogx(w, 20 * np.log10(np.abs(h)))
plt.axhline(-3, color='red')  # -3 dB magnitude
plt.axvline(10, color='green')  # cutoff frequency
plt.title('Magnitude-normalized Bessel filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.show()

# Plot the delay-normalized filter, showing the maximally-flat group delay
# at 0.1 seconds:

b, a = signal.bessel(5, 1/0.1, 'low', analog=True, norm='delay')
w, h = signal.freqs(b, a)
plt.figure()
plt.semilogx(w[1:], -np.diff(np.unwrap(np.angle(h)))/np.diff(w))
plt.axhline(0.1, color='red')  # 0.1 seconds group delay
plt.title('Bessel filter group delay')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Group delay [seconds]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.show()
