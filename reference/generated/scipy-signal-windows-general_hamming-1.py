# The Sentinel-1A/B Instrument Processing Facility uses generalized Hamming
# windows in the processing of spaceborne Synthetic Aperture Radar (SAR)
# data [Rea199fc456d6-3]_. The facility uses various values for the :math:`\alpha`
# parameter based on operating mode of the SAR instrument. Some common
# :math:`\alpha` values include 0.75, 0.7 and 0.52 [Rea199fc456d6-4]_. As an example, we
# plot these different windows.

from scipy.signal.windows import general_hamming
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt

fig1, spatial_plot = plt.subplots()
spatial_plot.set_title("Generalized Hamming Windows")
spatial_plot.set_ylabel("Amplitude")
spatial_plot.set_xlabel("Sample")

fig2, freq_plot = plt.subplots()
freq_plot.set_title("Frequency Responses")
freq_plot.set_ylabel("Normalized magnitude [dB]")
freq_plot.set_xlabel("Normalized frequency [cycles per sample]")

for alpha in [0.75, 0.7, 0.52]:
    window = general_hamming(41, alpha)
    spatial_plot.plot(window, label="{:.2f}".format(alpha))
    A = fft(window, 2048) / (len(window)/2.0)
    freq = np.linspace(-0.5, 0.5, len(A))
    response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
    freq_plot.plot(freq, response, label="{:.2f}".format(alpha))
freq_plot.legend(loc="upper right")
spatial_plot.legend(loc="upper right")
