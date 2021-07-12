from scipy.special import expit, logit

expit([-np.inf, -1.5, 0, 1.5, np.inf])
# array([ 0.        ,  0.18242552,  0.5       ,  0.81757448,  1.        ])

# `logit` is the inverse of `expit`:

logit(expit([-2.5, 0, 3.1, 5.0]))
# array([-2.5,  0. ,  3.1,  5. ])

# Plot expit(x) for x in [-6, 6]:

import matplotlib.pyplot as plt
x = np.linspace(-6, 6, 121)
y = expit(x)
plt.plot(x, y)
plt.grid()
plt.xlim(-6, 6)
plt.xlabel('x')
plt.title('expit(x)')
plt.show()
