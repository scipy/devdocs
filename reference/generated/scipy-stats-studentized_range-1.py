from scipy.stats import studentized_range
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# Calculate the first four moments:

k, df = 3, 10
mean, var, skew, kurt = studentized_range.stats(k, df, moments='mvsk')

# Display the probability density function (``pdf``):

x = np.linspace(studentized_range.ppf(0.01, k, df),
                studentized_range.ppf(0.99, k, df), 100)
ax.plot(x, studentized_range.pdf(x, k, df),
        'r-', lw=5, alpha=0.6, label='studentized_range pdf')

# Alternatively, the distribution object can be called (as a function)
# to fix the shape, location and scale parameters. This returns a "frozen"
# RV object holding the given parameters fixed.

# Freeze the distribution and display the frozen ``pdf``:

rv = studentized_range(k, df)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of ``cdf`` and ``ppf``:

vals = studentized_range.ppf([0.001, 0.5, 0.999], k, df)
np.allclose([0.001, 0.5, 0.999], studentized_range.cdf(vals, k, df))
# True

# Rather than using (``studentized_range.rvs``) to generate random variates,
# which is very slow for this distribution, we can approximate the inverse
# CDF using an interpolator, and then perform inverse transform sampling
# with this approximate inverse CDF.

# This distribution has an infinite but thin right tail, so we focus our
# attention on the leftmost 99.9 percent.

a, b = studentized_range.ppf([0, .999], k, df)
a, b
# 0, 7.41058083802274

from scipy.interpolate import interp1d
rng = np.random.default_rng()
xs = np.linspace(a, b, 50)
cdf = studentized_range.cdf(xs, k, df)
# # Create an interpolant of the inverse CDF
ppf = interp1d(cdf, xs, fill_value='extrapolate')
# # Perform inverse transform sampling using the interpolant
r = ppf(rng.uniform(size=1000))

# And compare the histogram:

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
