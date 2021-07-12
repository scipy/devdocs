import scipy.fft
x = np.mgrid[:3, :3, :3][0]
scipy.fft.fftn(x, axes=(1, 2))
# array([[[ 0.+0.j,   0.+0.j,   0.+0.j], # may vary
# [ 0.+0.j,   0.+0.j,   0.+0.j],
# [ 0.+0.j,   0.+0.j,   0.+0.j]],
# [[ 9.+0.j,   0.+0.j,   0.+0.j],
# [ 0.+0.j,   0.+0.j,   0.+0.j],
# [ 0.+0.j,   0.+0.j,   0.+0.j]],
# [[18.+0.j,   0.+0.j,   0.+0.j],
# [ 0.+0.j,   0.+0.j,   0.+0.j],
# [ 0.+0.j,   0.+0.j,   0.+0.j]]])
scipy.fft.fftn(x, (2, 2), axes=(0, 1))
# array([[[ 2.+0.j,  2.+0.j,  2.+0.j], # may vary
# [ 0.+0.j,  0.+0.j,  0.+0.j]],
# [[-2.+0.j, -2.+0.j, -2.+0.j],
# [ 0.+0.j,  0.+0.j,  0.+0.j]]])

import matplotlib.pyplot as plt
rng = np.random.default_rng()
[X, Y] = np.meshgrid(2 * np.pi * np.arange(200) / 12,
                     2 * np.pi * np.arange(200) / 34)
S = np.sin(X) + np.cos(Y) + rng.uniform(0, 1, X.shape)
FS = scipy.fft.fftn(S)
plt.imshow(np.log(np.abs(scipy.fft.fftshift(FS))**2))
# <matplotlib.image.AxesImage object at 0x...>
plt.show()
