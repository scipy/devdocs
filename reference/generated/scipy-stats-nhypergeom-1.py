from scipy.stats import nhypergeom
import matplotlib.pyplot as plt

# Suppose we have a collection of 20 animals, of which 7 are dogs.
# Then if we want to know the probability of finding a given number
# of dogs (successes) in a sample with exactly 12 animals that
# aren't dogs (failures), we can initialize a frozen distribution
# and plot the probability mass function:

M, n, r = [20, 7, 12]
rv = nhypergeom(M, n, r)
x = np.arange(0, n+2)
pmf_dogs = rv.pmf(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, pmf_dogs, 'bo')
ax.vlines(x, 0, pmf_dogs, lw=2)
ax.set_xlabel('# of dogs in our group with given 12 failures')
ax.set_ylabel('nhypergeom PMF')
plt.show()

# Instead of using a frozen distribution we can also use `nhypergeom`
# methods directly.  To for example obtain the probability mass
# function, use:

prb = nhypergeom.pmf(x, M, n, r)

# And to generate random numbers:

R = nhypergeom.rvs(M, n, r, size=10)

# To verify the relationship between `hypergeom` and `nhypergeom`, use:

from scipy.stats import hypergeom, nhypergeom
M, n, r = 45, 13, 8
k = 6
nhypergeom.pmf(k, M, n, r)
# 0.06180776620271643
hypergeom.pmf(k, M, n, k+r-1) * (M - n - (r-1)) / (M - (k+r-1))
# 0.06180776620271644
