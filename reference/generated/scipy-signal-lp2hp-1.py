from scipy import signal
import matplotlib.pyplot as plt

lp = signal.lti([1.0], [1.0, 1.0])
hp = signal.lti(*signal.lp2hp(lp.num, lp.den))
w, mag_lp, p_lp = lp.bode()
w, mag_hp, p_hp = hp.bode(w)

plt.plot(w, mag_lp, label='Lowpass')
plt.plot(w, mag_hp, label='Highpass')
plt.semilogx()
plt.grid()
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.legend()
