# Plot the window and its frequency response:

from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt

window = signal.windows.taylor(51, nbar=20, sll=100, norm=False)
plt.plot(window)
plt.title("Taylor window (100 dB)")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

plt.figure()
A = fft(window, 2048) / (len(window)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
plt.plot(freq, response)
plt.axis([-0.5, 0.5, -120, 0])
plt.title("Frequency response of the Taylor window (100 dB)")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")
