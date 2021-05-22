import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt

image = misc.ascent()
w = signal.windows.gaussian(51, 10.0)
image_new = signal.sepfir2d(image, w, w)

plt.figure()
plt.imshow(image)
plt.gray()
plt.title('Original image')
plt.show()

plt.figure()
plt.imshow(image_new)
plt.gray()
plt.title('Filtered image')
plt.show()
