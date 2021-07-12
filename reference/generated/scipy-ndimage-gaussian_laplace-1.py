from scipy import ndimage, misc
import matplotlib.pyplot as plt
ascent = misc.ascent()

fig = plt.figure()
plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)  # right side

result = ndimage.gaussian_laplace(ascent, sigma=1)
ax1.imshow(result)

result = ndimage.gaussian_laplace(ascent, sigma=3)
ax2.imshow(result)
plt.show()
