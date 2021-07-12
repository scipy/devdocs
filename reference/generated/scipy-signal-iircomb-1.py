# Design and plot notching comb filter at 20 Hz for a
# signal sampled at 200 Hz, using quality factor Q = 30

from scipy import signal
import matplotlib.pyplot as plt

fs = 200.0  # Sample frequency (Hz)
f0 = 20.0  # Frequency to be removed from signal (Hz)
Q = 30.0  # Quality factor
# Design notching comb filter
b, a = signal.iircomb(f0, Q, ftype='notch', fs=fs)

# Frequency response
freq, h = signal.freqz(b, a, fs=fs)
response = abs(h)
# To avoid divide by zero when graphing
response[response == 0] = 1e-20
# Plot
fig, ax = plt.subplots(2, 1, figsize=(8, 6))
ax[0].plot(freq, 20*np.log10(abs(response)), color='blue')
ax[0].set_title("Frequency Response")
ax[0].set_ylabel("Amplitude (dB)", color='blue')
ax[0].set_xlim([0, 100])
ax[0].set_ylim([-30, 10])
ax[0].grid()
ax[1].plot(freq, np.unwrap(np.angle(h))*180/np.pi, color='green')
ax[1].set_ylabel("Angle (degrees)", color='green')
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_xlim([0, 100])
ax[1].set_yticks([-90, -60, -30, 0, 30, 60, 90])
ax[1].set_ylim([-90, 90])
ax[1].grid()
plt.show()

# Design and plot peaking comb filter at 250 Hz for a
# signal sampled at 1000 Hz, using quality factor Q = 30

fs = 1000.0  # Sample frequency (Hz)
f0 = 250.0  # Frequency to be retained (Hz)
Q = 30.0  # Quality factor
# Design peaking filter
b, a = signal.iircomb(f0, Q, ftype='peak', fs=fs)

# Frequency response
freq, h = signal.freqz(b, a, fs=fs)
response = abs(h)
# To avoid divide by zero when graphing
response[response == 0] = 1e-20
# Plot
fig, ax = plt.subplots(2, 1, figsize=(8, 6))
ax[0].plot(freq, 20*np.log10(np.maximum(abs(h), 1e-5)), color='blue')
ax[0].set_title("Frequency Response")
ax[0].set_ylabel("Amplitude (dB)", color='blue')
ax[0].set_xlim([0, 500])
ax[0].set_ylim([-80, 10])
ax[0].grid()
ax[1].plot(freq, np.unwrap(np.angle(h))*180/np.pi, color='green')
ax[1].set_ylabel("Angle (degrees)", color='green')
ax[1].set_xlabel("Frequency (Hz)")
ax[1].set_xlim([0, 500])
ax[1].set_yticks([-90, -60, -30, 0, 30, 60, 90])
ax[1].set_ylim([-90, 90])
ax[1].grid()
plt.show()
