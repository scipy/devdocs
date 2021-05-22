from scipy.ndimage import gaussian_filter
a = np.arange(50, step=2).reshape((5,5))
a
# array([[ 0,  2,  4,  6,  8],
# [10, 12, 14, 16, 18],
# [20, 22, 24, 26, 28],
# [30, 32, 34, 36, 38],
# [40, 42, 44, 46, 48]])
gaussian_filter(a, sigma=1)
# array([[ 4,  6,  8,  9, 11],
# [10, 12, 14, 15, 17],
# [20, 22, 24, 25, 27],
# [29, 31, 33, 34, 36],
# [35, 37, 39, 40, 42]])

from scipy import misc
import matplotlib.pyplot as plt
fig = plt.figure()
plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)  # right side
ascent = misc.ascent()
result = gaussian_filter(ascent, sigma=5)
ax1.imshow(ascent)
ax2.imshow(result)
plt.show()
