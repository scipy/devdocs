# We can compare the window to `kaiser`, which was invented as an alternative
# that was easier to calculate [Re991e28c1f6b-3]_ (example adapted from
# `here <https://ccrma.stanford.edu/~jos/sasp/Kaiser_DPSS_Windows_Compared.html>`_):

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import windows, freqz
M = 51
fig, axes = plt.subplots(3, 2, figsize=(5, 7))
for ai, alpha in enumerate((1, 3, 5)):
    win_dpss = windows.dpss(M, alpha)
    beta = alpha*np.pi
    win_kaiser = windows.kaiser(M, beta)
    for win, c in ((win_dpss, 'k'), (win_kaiser, 'r')):
        win /= win.sum()
        axes[ai, 0].plot(win, color=c, lw=1.)
        axes[ai, 0].set(xlim=[0, M-1], title=r'$\alpha$ = %s' % alpha,
                        ylabel='Amplitude')
        w, h = freqz(win)
        axes[ai, 1].plot(w, 20 * np.log10(np.abs(h)), color=c, lw=1.)
        axes[ai, 1].set(xlim=[0, np.pi],
                        title=r'$\beta$ = %0.2f' % beta,
                        ylabel='Magnitude (dB)')
for ax in axes.ravel():
    ax.grid(True)
axes[2, 1].legend(['DPSS', 'Kaiser'])
fig.tight_layout()
plt.show()

# And here are examples of the first four windows, along with their
# concentration ratios:

M = 512
NW = 2.5
win, eigvals = windows.dpss(M, NW, 4, return_ratios=True)
fig, ax = plt.subplots(1)
ax.plot(win.T, linewidth=1.)
ax.set(xlim=[0, M-1], ylim=[-0.1, 0.1], xlabel='Samples',
       title='DPSS, M=%d, NW=%0.1f' % (M, NW))
ax.legend(['win[%d] (%0.4f)' % (ii, ratio)
           for ii, ratio in enumerate(eigvals)])
fig.tight_layout()
plt.show()

# Using a standard :math:`l_{\infty}` norm would produce two unity values
# for even `M`, but only one unity value for odd `M`. This produces uneven
# window power that can be counteracted by the approximate correction
# ``M**2/float(M**2+NW)``, which can be selected by using
# ``norm='approximate'`` (which is the same as ``norm=None`` when
# ``Kmax=None``, as is the case here). Alternatively, the slower
# ``norm='subsample'`` can be used, which uses subsample shifting in the
# frequency domain (FFT) to compute the correction:

Ms = np.arange(1, 41)
factors = (50, 20, 10, 5, 2.0001)
energy = np.empty((3, len(Ms), len(factors)))
for mi, M in enumerate(Ms):
    for fi, factor in enumerate(factors):
        NW = M / float(factor)
        # Corrected using empirical approximation (default)
        win = windows.dpss(M, NW)
        energy[0, mi, fi] = np.sum(win ** 2) / np.sqrt(M)
        # Corrected using subsample shifting
        win = windows.dpss(M, NW, norm='subsample')
        energy[1, mi, fi] = np.sum(win ** 2) / np.sqrt(M)
        # Uncorrected (using l-infinity norm)
        win /= win.max()
        energy[2, mi, fi] = np.sum(win ** 2) / np.sqrt(M)
fig, ax = plt.subplots(1)
hs = ax.plot(Ms, energy[2], '-o', markersize=4,
             markeredgecolor='none')
leg = [hs[-1]]
for hi, hh in enumerate(hs):
    h1 = ax.plot(Ms, energy[0, :, hi], '-o', markersize=4,
                 color=hh.get_color(), markeredgecolor='none',
                 alpha=0.66)
    h2 = ax.plot(Ms, energy[1, :, hi], '-o', markersize=4,
                 color=hh.get_color(), markeredgecolor='none',
                 alpha=0.33)
    if hi == len(hs) - 1:
        leg.insert(0, h1[0])
        leg.insert(0, h2[0])
ax.set(xlabel='M (samples)', ylabel=r'Power / $\sqrt{M}$')
ax.legend(leg, ['Uncorrected', r'Corrected: $\frac{M^2}{M^2+NW}$',
                'Corrected (subsample)'])
fig.tight_layout()
