# The following will be used in the examples:

from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt

# For the first example, we'll plot the waveform for a linear chirp
# from 6 Hz to 1 Hz over 10 seconds:

t = np.linspace(0, 10, 1500)
w = chirp(t, f0=6, f1=1, t1=10, method='linear')
plt.plot(t, w)
plt.title("Linear Chirp, f(0)=6, f(10)=1")
plt.xlabel('t (sec)')
plt.show()

# For the remaining examples, we'll use higher frequency ranges,
# and demonstrate the result using `scipy.signal.spectrogram`.
# We'll use a 4 second interval sampled at 7200 Hz.

fs = 7200
T = 4
t = np.arange(0, int(T*fs)) / fs

# We'll use this function to plot the spectrogram in each example.

def plot_spectrogram(title, w, fs):
    ff, tt, Sxx = spectrogram(w, fs=fs, nperseg=256, nfft=576)
    plt.pcolormesh(tt, ff[:145], Sxx[:145], cmap='gray_r', shading='gouraud')
    plt.title(title)
    plt.xlabel('t (sec)')
    plt.ylabel('Frequency (Hz)')
    plt.grid()
# ...

# Quadratic chirp from 1500 Hz to 250 Hz
# (vertex of the parabolic curve of the frequency is at t=0):

w = chirp(t, f0=1500, f1=250, t1=T, method='quadratic')
plot_spectrogram(f'Quadratic Chirp, f(0)=1500, f({T})=250', w, fs)
plt.show()

# Quadratic chirp from 1500 Hz to 250 Hz
# (vertex of the parabolic curve of the frequency is at t=T):

w = chirp(t, f0=1500, f1=250, t1=T, method='quadratic',
          vertex_zero=False)
plot_spectrogram(f'Quadratic Chirp, f(0)=1500, f({T})=250\n' +
                 '(vertex_zero=False)', w, fs)
plt.show()

# Logarithmic chirp from 1500 Hz to 250 Hz:

w = chirp(t, f0=1500, f1=250, t1=T, method='logarithmic')
plot_spectrogram(f'Logarithmic Chirp, f(0)=1500, f({T})=250', w, fs)
plt.show()

# Hyperbolic chirp from 1500 Hz to 250 Hz:

w = chirp(t, f0=1500, f1=250, t1=T, method='hyperbolic')
plot_spectrogram(f'Hyperbolic Chirp, f(0)=1500, f({T})=250', w, fs)
plt.show()
