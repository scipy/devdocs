from scipy import ndimage, misc
import numpy.fft
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2)
plt.gray()  # show the filtered result in grayscale
ascent = misc.ascent()
input_ = numpy.fft.fft2(ascent)
result = ndimage.fourier_uniform(input_, size=20)
result = numpy.fft.ifft2(result)
ax1.imshow(ascent)
ax2.imshow(result.real)  # the imaginary part is an artifact
plt.show()
