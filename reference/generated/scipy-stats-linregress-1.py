import matplotlib.pyplot as plt
from scipy import stats
rng = np.random.default_rng()

# Generate some data:

x = rng.random(10)
y = 1.6*x + rng.random(10)

# Perform the linear regression:

res = stats.linregress(x, y)

# Coefficient of determination (R-squared):

print(f"R-squared: {res.rvalue**2:.6f}")
# R-squared: 0.717533

# Plot the data along with the fitted line:

plt.plot(x, y, 'o', label='original data')
plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
plt.legend()
plt.show()

# Calculate 95% confidence interval on slope and intercept:

# Two-sided inverse Students t-distribution
# p - probability, df - degrees of freedom
from scipy.stats import t
tinv = lambda p, df: abs(t.ppf(p/2, df))

ts = tinv(0.05, len(x)-2)
print(f"slope (95%): {res.slope:.6f} +/- {ts*res.stderr:.6f}")
# slope (95%): 1.453392 +/- 0.743465
print(f"intercept (95%): {res.intercept:.6f}"
      f" +/- {ts*res.intercept_stderr:.6f}")
# intercept (95%): 0.616950 +/- 0.544475
