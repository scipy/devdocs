from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.ticker

wp = 0.2
ws = 0.3
gpass = 1
gstop = 40

system = signal.iirdesign(wp, ws, gpass, gstop)
w, h = signal.freqz(*system)

fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
ax1.grid()
ax1.set_ylim([-120, 20])
ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid()
ax2.axis('tight')
ax2.set_ylim([-6, 1])
nticks = 8
ax1.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
ax2.yaxis.set_major_locator(matplotlib.ticker.LinearLocator(nticks))
