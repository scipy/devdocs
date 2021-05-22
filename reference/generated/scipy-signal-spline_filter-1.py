# We can filter an multi dimentional signal (ex: 2D image) using cubic
# B-spline filter:

from scipy.signal import spline_filter
import matplotlib.pyplot as plt
orig_img = np.eye(20)  # create an image
orig_img[10, :] = 1.0
sp_filter = spline_filter(orig_img, lmbda=0.1)
f, ax = plt.subplots(1, 2, sharex=True)
for ind, data in enumerate([[orig_img, "original image"],
                            [sp_filter, "spline filter"]]):
    ax[ind].imshow(data[0], cmap='gray_r')
    ax[ind].set_title(data[1])
plt.tight_layout()
plt.show()
