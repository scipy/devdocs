# In Fisher's definiton, the kurtosis of the normal distribution is zero.
# In the following example, the kurtosis is close to zero, because it was
# calculated from the dataset, not from the continuous distribution.

from scipy.stats import norm, kurtosis
data = norm.rvs(size=1000, random_state=3)
kurtosis(data)
# -0.06928694200380558

# The distribution with a higher kurtosis has a heavier tail.
# The zero valued kurtosis of the normal distribution in Fisher's definition
# can serve as a reference point.

import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import kurtosis

x = np.linspace(-5, 5, 100)
ax = plt.subplot()
distnames = ['laplace', 'norm', 'uniform']

for distname in distnames:
    if distname == 'uniform':
        dist = getattr(stats, distname)(loc=-2, scale=4)
    else:
        dist = getattr(stats, distname)
    data = dist.rvs(size=1000)
    kur = kurtosis(data, fisher=True)
    y = dist.pdf(x)
    ax.plot(x, y, label="{}, {}".format(distname, round(kur, 3)))
    ax.legend()

# The Laplace distribution has a heavier tail than the normal distribution.
# The uniform distribution (which has negative kurtosis) has the thinnest
# tail.
