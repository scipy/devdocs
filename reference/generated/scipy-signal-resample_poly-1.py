# By default, the end of the resampled data rises to meet the first
# sample of the next cycle for the FFT method, and gets closer to zero
# for the polyphase method:

from scipy import signal

x = np.linspace(0, 10, 20, endpoint=False)
y = np.cos(-x**2/6.0)
f_fft = signal.resample(y, 100)
f_poly = signal.resample_poly(y, 100, 20)
xnew = np.linspace(0, 10, 100, endpoint=False)

import matplotlib.pyplot as plt
plt.plot(xnew, f_fft, 'b.-', xnew, f_poly, 'r.-')
plt.plot(x, y, 'ko-')
plt.plot(10, y[0], 'bo', 10, 0., 'ro')  # boundaries
plt.legend(['resample', 'resamp_poly', 'data'], loc='best')
plt.show()

# This default behaviour can be changed by using the padtype option:

import numpy as np
from scipy import signal

N = 5
x = np.linspace(0, 1, N, endpoint=False)
y = 2 + x**2 - 1.7*np.sin(x) + .2*np.cos(11*x)
y2 = 1 + x**3 + 0.1*np.sin(x) + .1*np.cos(11*x)
Y = np.stack([y, y2], axis=-1)
up = 4
xr = np.linspace(0, 1, N*up, endpoint=False)

y2 = signal.resample_poly(Y, up, 1, padtype='constant')
y3 = signal.resample_poly(Y, up, 1, padtype='mean')
y4 = signal.resample_poly(Y, up, 1, padtype='line')

import matplotlib.pyplot as plt
for i in [0,1]:
    plt.figure()
    plt.plot(xr, y4[:,i], 'g.', label='line')
    plt.plot(xr, y3[:,i], 'y.', label='mean')
    plt.plot(xr, y2[:,i], 'r.', label='constant')
    plt.plot(x, Y[:,i], 'k-')
    plt.legend()
plt.show()
