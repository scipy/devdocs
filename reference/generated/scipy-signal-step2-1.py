from scipy import signal
import matplotlib.pyplot as plt
lti = signal.lti([1.0], [1.0, 1.0])
t, y = signal.step2(lti)
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step response for 1. Order Lowpass')
plt.grid()
