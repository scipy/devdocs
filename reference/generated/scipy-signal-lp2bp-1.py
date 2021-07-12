from scipy import signal
import matplotlib.pyplot as plt

lp = signal.lti([1.0], [1.0, 1.0])
bp = signal.lti(*signal.lp2bp(lp.num, lp.den))
w, mag_lp, p_lp = lp.bode()
w, mag_bp, p_bp = bp.bode(w)

plt.plot(w, mag_lp, label='Lowpass')
plt.plot(w, mag_bp, label='Bandpass')
plt.semilogx()
plt.grid()
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.legend()
