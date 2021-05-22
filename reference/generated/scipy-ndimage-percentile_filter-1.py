from scipy import ndimage, misc
import matplotlib.pyplot as plt
fig = plt.figure()
plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)  # right side
ascent = misc.ascent()
result = ndimage.percentile_filter(ascent, percentile=20, size=20)
ax1.imshow(ascent)
ax2.imshow(result)
plt.show()
