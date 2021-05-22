from scipy import signal
import matplotlib.pyplot as plt

butter = signal.dlti(*signal.butter(3, 0.5))
t, y = signal.dimpulse(butter, n=25)
plt.step(t, np.squeeze(y))
plt.grid()
plt.xlabel('n [samples]')
plt.ylabel('Amplitude')
