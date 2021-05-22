# In this example we use the Hilbert transform to determine the amplitude
# envelope and instantaneous frequency of an amplitude-modulated signal.

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp

duration = 1.0
fs = 400.0
samples = int(fs*duration)
t = np.arange(samples) / fs

# We create a chirp of which the frequency increases from 20 Hz to 100 Hz and
# apply an amplitude modulation.

signal = chirp(t, 20.0, t[-1], 100.0)
signal *= (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t) )

# The amplitude envelope is given by magnitude of the analytic signal. The
# instantaneous frequency can be obtained by differentiating the
# instantaneous phase in respect to time. The instantaneous phase corresponds
# to the phase angle of the analytic signal.

analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = (np.diff(instantaneous_phase) /
                           (2.0*np.pi) * fs)

fig, (ax0, ax1) = plt.subplots(nrows=2)
ax0.plot(t, signal, label='signal')
ax0.plot(t, amplitude_envelope, label='envelope')
ax0.set_xlabel("time in seconds")
ax0.legend()
ax1.plot(t[1:], instantaneous_frequency)
ax1.set_xlabel("time in seconds")
ax1.set_ylim(0.0, 120.0)
fig.tight_layout()
