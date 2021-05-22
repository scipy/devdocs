from scipy import signal
import matplotlib.pyplot as plt

lp = signal.lti([1.0], [1.0, 1.5])
bs = signal.lti(*signal.lp2bs(lp.num, lp.den))
w, mag_lp, p_lp = lp.bode()
w, mag_bs, p_bs = bs.bode(w)
plt.plot(w, mag_lp, label='Lowpass')
plt.plot(w, mag_bs, label='Bandstop')
plt.semilogx()
plt.grid()
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.legend()
