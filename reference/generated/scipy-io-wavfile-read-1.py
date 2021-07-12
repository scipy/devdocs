from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io

# Get the filename for an example .wav file from the tests/data directory.

data_dir = pjoin(dirname(scipy.io.__file__), 'tests', 'data')
wav_fname = pjoin(data_dir, 'test-44100Hz-2ch-32bit-float-be.wav')

# Load the .wav file contents.

samplerate, data = wavfile.read(wav_fname)
print(f"number of channels = {data.shape[1]}")
# number of channels = 2
length = data.shape[0] / samplerate
print(f"length = {length}s")
# length = 0.01s

# Plot the waveform.

import matplotlib.pyplot as plt
import numpy as np
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
