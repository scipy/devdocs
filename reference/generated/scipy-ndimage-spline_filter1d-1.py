# We can filter an image using 1-D spline along the given axis:

from scipy.ndimage import spline_filter1d
import matplotlib.pyplot as plt
orig_img = np.eye(20)  # create an image
orig_img[10, :] = 1.0
sp_filter_axis_0 = spline_filter1d(orig_img, axis=0)
sp_filter_axis_1 = spline_filter1d(orig_img, axis=1)
f, ax = plt.subplots(1, 3, sharex=True)
for ind, data in enumerate([[orig_img, "original image"],
            [sp_filter_axis_0, "spline filter (axis=0)"],
            [sp_filter_axis_1, "spline filter (axis=1)"]]):
    ax[ind].imshow(data[0], cmap='gray_r')
    ax[ind].set_title(data[1])
plt.tight_layout()
plt.show()
