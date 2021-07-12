from scipy import special
import matplotlib.pyplot as plt

# We can initialize a variable ``p`` as a Gegenbauer polynomial using the
# `gegenbauer` function and evaluate at a point ``x = 1``.

p = special.gegenbauer(3, 0.5, monic=False)
p
# poly1d([ 2.5,  0. , -1.5,  0. ])
p(1)
# 1.0

# To evaluate ``p`` at various points ``x`` in the interval ``(-3, 3)``,
# simply pass an array ``x`` to ``p`` as follows:

x = np.linspace(-3, 3, 400)
y = p(x)

# We can then visualize ``x, y`` using `matplotlib.pyplot`.

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Gegenbauer (ultraspherical) polynomial of degree 3")
ax.set_xlabel("x")
ax.set_ylabel("G_3(x)")
plt.show()
