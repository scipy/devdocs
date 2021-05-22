from scipy import signal
import matplotlib.pyplot as plt

lp = signal.lti([1.0], [1.0, 1.0])
lp2 = signal.lti(*signal.lp2lp(lp.num, lp.den, 2))
w, mag_lp, p_lp = lp.bode()
w, mag_lp2, p_lp2 = lp2.bode(w)

plt.plot(w, mag_lp, label='Lowpass')
plt.plot(w, mag_lp2, label='Transformed Lowpass')
plt.semilogx()
plt.grid()
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.legend()
