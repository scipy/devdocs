from scipy import stats
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, num=150)
y = x + np.random.normal(size=x.size)
y[11:15] += 10  # add outliers
y[-5:] -= 7

# Compute the slope and intercept.  For comparison, also compute the
# least-squares fit with `linregress`:

res = stats.siegelslopes(y, x)
lsq_res = stats.linregress(x, y)

# Plot the results. The Siegel regression line is shown in red. The green
# line shows the least-squares fit for comparison.

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'b.')
ax.plot(x, res[1] + res[0] * x, 'r-')
ax.plot(x, lsq_res[1] + lsq_res[0] * x, 'g-')
plt.show()
