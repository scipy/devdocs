# Design a 4th-order digital Butterworth filter with cut-off of 100 Hz in a
# system with sample rate of 1000 Hz, and plot the frequency response:

from scipy import signal
z, p, k = signal.butter(4, 100, output='zpk', fs=1000)
w, h = signal.freqz_zpk(z, p, k, fs=1000)

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('Digital filter frequency response')

ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [Hz]')
ax1.grid()

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle [radians]', color='g')

plt.axis('tight')
plt.show()
