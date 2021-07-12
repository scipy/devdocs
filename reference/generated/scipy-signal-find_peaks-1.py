# To demonstrate this function's usage we use a signal `x` supplied with
# SciPy (see `scipy.misc.electrocardiogram`). Let's find all peaks (local
# maxima) in `x` whose amplitude lies above 0.

import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
x = electrocardiogram()[2000:4000]
peaks, _ = find_peaks(x, height=0)
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.plot(np.zeros_like(x), "--", color="gray")
plt.show()

# We can select peaks below 0 with ``height=(None, 0)`` or use arrays matching
# `x` in size to reflect a changing condition for different parts of the
# signal.

border = np.sin(np.linspace(0, 3 * np.pi, x.size))
peaks, _ = find_peaks(x, height=(-border, border))
plt.plot(x)
plt.plot(-border, "--", color="gray")
plt.plot(border, ":", color="gray")
plt.plot(peaks, x[peaks], "x")
plt.show()

# Another useful condition for periodic signals can be given with the
# `distance` argument. In this case, we can easily select the positions of
# QRS complexes within the electrocardiogram (ECG) by demanding a distance of
# at least 150 samples.

peaks, _ = find_peaks(x, distance=150)
np.diff(peaks)
# array([186, 180, 177, 171, 177, 169, 167, 164, 158, 162, 172])
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.show()

# Especially for noisy signals peaks can be easily grouped by their
# prominence (see `peak_prominences`). E.g., we can select all peaks except
# for the mentioned QRS complexes by limiting the allowed prominence to 0.6.

peaks, properties = find_peaks(x, prominence=(None, 0.6))
properties["prominences"].max()
# 0.5049999999999999
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.show()

# And, finally, let's examine a different section of the ECG which contains
# beat forms of different shape. To select only the atypical heart beats, we
# combine two conditions: a minimal prominence of 1 and width of at least 20
# samples.

x = electrocardiogram()[17000:18000]
peaks, properties = find_peaks(x, prominence=1, width=20)
properties["prominences"], properties["widths"]
# (array([1.495, 2.3  ]), array([36.93773946, 39.32723577]))
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.vlines(x=peaks, ymin=x[peaks] - properties["prominences"],
           ymax = x[peaks], color = "C1")
plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
           xmax=properties["right_ips"], color = "C1")
plt.show()
