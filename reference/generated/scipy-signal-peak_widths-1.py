from scipy.signal import chirp, find_peaks, peak_widths
import matplotlib.pyplot as plt

# Create a test signal with two overlayed harmonics

x = np.linspace(0, 6 * np.pi, 1000)
x = np.sin(x) + 0.6 * np.sin(2.6 * x)

# Find all peaks and calculate their widths at the relative height of 0.5
# (contour line at half the prominence height) and 1 (at the lowest contour
# line at full prominence height).

peaks, _ = find_peaks(x)
results_half = peak_widths(x, peaks, rel_height=0.5)
results_half[0]  # widths
# array([ 64.25172825,  41.29465463,  35.46943289, 104.71586081,
# 35.46729324,  41.30429622, 181.93835853,  45.37078546])
results_full = peak_widths(x, peaks, rel_height=1)
results_full[0]  # widths
# array([181.9396084 ,  72.99284945,  61.28657872, 373.84622694,
# 61.78404617,  72.48822812, 253.09161876,  79.36860878])

# Plot signal, peaks and contour lines at which the widths where calculated

plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.hlines(*results_half[1:], color="C2")
plt.hlines(*results_full[1:], color="C3")
plt.show()
