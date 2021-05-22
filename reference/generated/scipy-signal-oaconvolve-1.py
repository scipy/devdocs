# Convolve a 100,000 sample signal with a 512-sample filter.

from scipy import signal
rng = np.random.default_rng()
sig = rng.standard_normal(100000)
filt = signal.firwin(512, 0.01)
fsig = signal.oaconvolve(sig, filt)

import matplotlib.pyplot as plt
fig, (ax_orig, ax_mag) = plt.subplots(2, 1)
ax_orig.plot(sig)
ax_orig.set_title('White noise')
ax_mag.plot(fsig)
ax_mag.set_title('Filtered noise')
fig.tight_layout()
fig.show()
