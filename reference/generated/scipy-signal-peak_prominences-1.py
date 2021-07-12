from scipy.signal import find_peaks, peak_prominences
import matplotlib.pyplot as plt

# Create a test signal with two overlayed harmonics

x = np.linspace(0, 6 * np.pi, 1000)
x = np.sin(x) + 0.6 * np.sin(2.6 * x)

# Find all peaks and calculate prominences

peaks, _ = find_peaks(x)
prominences = peak_prominences(x, peaks)[0]
prominences
# array([1.24159486, 0.47840168, 0.28470524, 3.10716793, 0.284603  ,
# 0.47822491, 2.48340261, 0.47822491])

# Calculate the height of each peak's contour line and plot the results

contour_heights = x[peaks] - prominences
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.vlines(x=peaks, ymin=contour_heights, ymax=x[peaks])
plt.show()

# Let's evaluate a second example that demonstrates several edge cases for
# one peak at index 5.

x = np.array([0, 1, 0, 3, 1, 3, 0, 4, 0])
peaks = np.array([5])
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.show()
peak_prominences(x, peaks)  # -> (prominences, left_bases, right_bases)
# (array([3.]), array([2]), array([6]))

# Note how the peak at index 3 of the same height is not considered as a
# border while searching for the left base. Instead, two minima at 0 and 2
# are found in which case the one closer to the evaluated peak is always
# chosen. On the right side, however, the base must be placed at 6 because the
# higher peak represents the right border to the evaluated area.

peak_prominences(x, peaks, wlen=3.1)
# (array([2.]), array([4]), array([6]))

# Here, we restricted the algorithm to a window from 3 to 7 (the length is 5
# samples because `wlen` was rounded up to the next odd integer). Thus, the
# only two candidates in the evaluated area are the two neighboring samples
# and a smaller prominence is calculated.
