from scipy.special import smirnov

# Show the probability of a gap at least as big as 0, 0.5 and 1.0 for a sample of size 5

smirnov(5, [0, 0.5, 1.0])
# array([ 1.   ,  0.056,  0.   ])

# Compare a sample of size 5 drawn from a source N(0.5, 1) distribution against
# a target N(0, 1) CDF.

from scipy.stats import norm
rng = np.random.default_rng()
n = 5
gendist = norm(0.5, 1)       # Normal distribution, mean 0.5, stddev 1
x = np.sort(gendist.rvs(size=n, random_state=rng))
x
# array([-1.3922078 , -0.13526532,  0.1371477 ,  0.18981686,  1.81948167])
target = norm(0, 1)
cdfs = target.cdf(x)
cdfs
# array([0.08192974, 0.44620105, 0.55454297, 0.57527368, 0.96558101])
# # Construct the Empirical CDF and the K-S statistics (Dn+, Dn-, Dn)
ecdfs = np.arange(n+1, dtype=float)/n
cols = np.column_stack([x, ecdfs[1:], cdfs, cdfs - ecdfs[:n], ecdfs[1:] - cdfs])
np.set_printoptions(precision=3)
cols
# array([[-1.392,  0.2  ,  0.082,  0.082,  0.118],
# [-0.135,  0.4  ,  0.446,  0.246, -0.046],
# [ 0.137,  0.6  ,  0.555,  0.155,  0.045],
# [ 0.19 ,  0.8  ,  0.575, -0.025,  0.225],
# [ 1.819,  1.   ,  0.966,  0.166,  0.034]])
gaps = cols[:, -2:]
Dnpm = np.max(gaps, axis=0)
print('Dn-=%f, Dn+=%f' % (Dnpm[0], Dnpm[1]))
# Dn-=0.246201, Dn+=0.224726
probs = smirnov(n, Dnpm)
print(chr(10).join(['For a sample of size %d drawn from a N(0, 1) distribution:' % n,
     ' Smirnov n=%d: Prob(Dn- >= %f) = %.4f' % (n, Dnpm[0], probs[0]),
     ' Smirnov n=%d: Prob(Dn+ >= %f) = %.4f' % (n, Dnpm[1], probs[1])]))
# For a sample of size 5 drawn from a N(0, 1) distribution:
# Smirnov n=5: Prob(Dn- >= 0.246201) = 0.4713
# Smirnov n=5: Prob(Dn+ >= 0.224726) = 0.5243

# Plot the Empirical CDF against the target N(0, 1) CDF

import matplotlib.pyplot as plt
plt.step(np.concatenate([[-3], x]), ecdfs, where='post', label='Empirical CDF')
x3 = np.linspace(-3, 3, 100)
plt.plot(x3, target.cdf(x3), label='CDF for N(0, 1)')
plt.ylim([0, 1]); plt.grid(True); plt.legend();
# # Add vertical lines marking Dn+ and Dn-
iminus, iplus = np.argmax(gaps, axis=0)
plt.vlines([x[iminus]], ecdfs[iminus], cdfs[iminus], color='r', linestyle='dashed', lw=4)
plt.vlines([x[iplus]], cdfs[iplus], ecdfs[iplus+1], color='m', linestyle='dashed', lw=4)
plt.show()
