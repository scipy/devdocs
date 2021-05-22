from scipy import special
import matplotlib.pyplot as plt
import numpy as np

p_monic = special.hermite(3, monic=True)
p_monic
# poly1d([ 1. ,  0. , -1.5,  0. ])
p_monic(1)
# -0.49999999999999983
x = np.linspace(-3, 3, 400)
y = p_monic(x)
plt.plot(x, y)
plt.title("Monic Hermite polynomial of degree 3")
plt.xlabel("x")
plt.ylabel("H_3(x)")
plt.show()
