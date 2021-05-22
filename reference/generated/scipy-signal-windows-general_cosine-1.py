# Heinzel describes a flat-top window named "HFT90D" with formula: [Ra1c31527b55d-2]_

# .. math::  w_j = 1 - 1.942604 \cos(z) + 1.340318 \cos(2z)
# - 0.440811 \cos(3z) + 0.043097 \cos(4z)

# where

# .. math::  z = \frac{2 \pi j}{N}, j = 0...N - 1

# Since this uses the convention of starting at the origin, to reproduce the
# window, we need to convert every other coefficient to a positive number:

HFT90D = [1, 1.942604, 1.340318, 0.440811, 0.043097]

# The paper states that the highest sidelobe is at -90.2 dB.  Reproduce
# Figure 42 by plotting the window and its frequency response, and confirm
# the sidelobe level in red:

from scipy.signal.windows import general_cosine
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt

window = general_cosine(1000, HFT90D, sym=False)
plt.plot(window)
plt.title("HFT90D window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

plt.figure()
A = fft(window, 10000) / (len(window)/2.0)
freq = np.linspace(-0.5, 0.5, len(A))
response = np.abs(fftshift(A / abs(A).max()))
response = 20 * np.log10(np.maximum(response, 1e-10))
plt.plot(freq, response)
plt.axis([-50/1000, 50/1000, -140, 0])
plt.title("Frequency response of the HFT90D window")
plt.ylabel("Normalized magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")
plt.axhline(-90.2, color='red')
plt.show()
