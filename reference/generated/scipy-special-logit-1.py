from scipy.special import logit, expit

logit([0, 0.25, 0.5, 0.75, 1])
# array([       -inf, -1.09861229,  0.        ,  1.09861229,         inf])

# `expit` is the inverse of `logit`:

expit(logit([0.1, 0.75, 0.999]))
# array([ 0.1  ,  0.75 ,  0.999])

# Plot logit(x) for x in [0, 1]:

import matplotlib.pyplot as plt
x = np.linspace(0, 1, 501)
y = logit(x)
plt.plot(x, y)
plt.grid()
plt.ylim(-6, 6)
plt.xlabel('x')
plt.title('logit(x)')
plt.show()
