from scipy.signal import sosfiltfilt, butter
import matplotlib.pyplot as plt
rng = np.random.default_rng()

# Create an interesting signal to filter.

n = 201
t = np.linspace(0, 1, n)
x = 1 + (t < 0.5) - 0.25*t**2 + 0.05*rng.standard_normal(n)

# Create a lowpass Butterworth filter, and use it to filter `x`.

sos = butter(4, 0.125, output='sos')
y = sosfiltfilt(sos, x)

# For comparison, apply an 8th order filter using `sosfilt`.  The filter
# is initialized using the mean of the first four values of `x`.

from scipy.signal import sosfilt, sosfilt_zi
sos8 = butter(8, 0.125, output='sos')
zi = x[:4].mean() * sosfilt_zi(sos8)
y2, zo = sosfilt(sos8, x, zi=zi)

# Plot the results.  Note that the phase of `y` matches the input, while
# `y2` has a significant phase delay.

plt.plot(t, x, alpha=0.5, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.plot(t, y2, label='y2(t)')
plt.legend(framealpha=1, shadow=True)
plt.grid(alpha=0.25)
plt.xlabel('t')
plt.show()
