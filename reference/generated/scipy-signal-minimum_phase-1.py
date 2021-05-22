# Create an optimal linear-phase filter, then convert it to minimum phase:

from scipy.signal import remez, minimum_phase, freqz, group_delay
import matplotlib.pyplot as plt
freq = [0, 0.2, 0.3, 1.0]
desired = [1, 0]
h_linear = remez(151, freq, desired, Hz=2.)

# Convert it to minimum phase:

h_min_hom = minimum_phase(h_linear, method='homomorphic')
h_min_hil = minimum_phase(h_linear, method='hilbert')

# Compare the three filters:

fig, axs = plt.subplots(4, figsize=(4, 8))
for h, style, color in zip((h_linear, h_min_hom, h_min_hil),
                           ('-', '-', '--'), ('k', 'r', 'c')):
    w, H = freqz(h)
    w, gd = group_delay((h, 1))
    w /= np.pi
    axs[0].plot(h, color=color, linestyle=style)
    axs[1].plot(w, np.abs(H), color=color, linestyle=style)
    axs[2].plot(w, 20 * np.log10(np.abs(H)), color=color, linestyle=style)
    axs[3].plot(w, gd, color=color, linestyle=style)
for ax in axs:
    ax.grid(True, color='0.5')
    ax.fill_between(freq[1:3], *ax.get_ylim(), color='#ffeeaa', zorder=1)
axs[0].set(xlim=[0, len(h_linear) - 1], ylabel='Amplitude', xlabel='Samples')
axs[1].legend(['Linear', 'Min-Hom', 'Min-Hil'], title='Phase')
for ax, ylim in zip(axs[1:], ([0, 1.1], [-150, 10], [-60, 60])):
    ax.set(xlim=[0, 1], ylim=ylim, xlabel='Frequency')
axs[1].set(ylabel='Magnitude')
axs[2].set(ylabel='Magnitude (dB)')
axs[3].set(ylabel='Group delay')
plt.tight_layout()
