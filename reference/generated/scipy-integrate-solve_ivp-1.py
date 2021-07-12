# Basic exponential decay showing automatically chosen time points.

from scipy.integrate import solve_ivp
def exponential_decay(t, y): return -0.5 * y
sol = solve_ivp(exponential_decay, [0, 10], [2, 4, 8])
print(sol.t)
# [ 0.          0.11487653  1.26364188  3.06061781  4.81611105  6.57445806
# 8.33328988 10.        ]
print(sol.y)
# [[2.         1.88836035 1.06327177 0.43319312 0.18017253 0.07483045
# 0.03107158 0.01350781]
# [4.         3.7767207  2.12654355 0.86638624 0.36034507 0.14966091
# 0.06214316 0.02701561]
# [8.         7.5534414  4.25308709 1.73277247 0.72069014 0.29932181
# 0.12428631 0.05403123]]

# Specifying points where the solution is desired.

sol = solve_ivp(exponential_decay, [0, 10], [2, 4, 8],
                t_eval=[0, 1, 2, 4, 10])
print(sol.t)
# [ 0  1  2  4 10]
print(sol.y)
# [[2.         1.21305369 0.73534021 0.27066736 0.01350938]
# [4.         2.42610739 1.47068043 0.54133472 0.02701876]
# [8.         4.85221478 2.94136085 1.08266944 0.05403753]]

# Cannon fired upward with terminal event upon impact. The ``terminal`` and
# ``direction`` fields of an event are applied by monkey patching a function.
# Here ``y[0]`` is position and ``y[1]`` is velocity. The projectile starts
# at position 0 with velocity +10. Note that the integration never reaches
# t=100 because the event is terminal.

def upward_cannon(t, y): return [y[1], -0.5]
def hit_ground(t, y): return y[0]
hit_ground.terminal = True
hit_ground.direction = -1
sol = solve_ivp(upward_cannon, [0, 100], [0, 10], events=hit_ground)
print(sol.t_events)
# [array([40.])]
print(sol.t)
# [0.00000000e+00 9.99900010e-05 1.09989001e-03 1.10988901e-02
# 1.11088891e-01 1.11098890e+00 1.11099890e+01 4.00000000e+01]

# Use `dense_output` and `events` to find position, which is 100, at the apex
# of the cannonball's trajectory. Apex is not defined as terminal, so both
# apex and hit_ground are found. There is no information at t=20, so the sol
# attribute is used to evaluate the solution. The sol attribute is returned
# by setting ``dense_output=True``. Alternatively, the `y_events` attribute
# can be used to access the solution at the time of the event.

def apex(t, y): return y[1]
sol = solve_ivp(upward_cannon, [0, 100], [0, 10],
                events=(hit_ground, apex), dense_output=True)
print(sol.t_events)
# [array([40.]), array([20.])]
print(sol.t)
# [0.00000000e+00 9.99900010e-05 1.09989001e-03 1.10988901e-02
# 1.11088891e-01 1.11098890e+00 1.11099890e+01 4.00000000e+01]
print(sol.sol(sol.t_events[1][0]))
# [100.   0.]
print(sol.y_events)
# [array([[-5.68434189e-14, -1.00000000e+01]]), array([[1.00000000e+02, 1.77635684e-15]])]

# As an example of a system with additional parameters, we'll implement
# the Lotka-Volterra equations [R179348322575-12]_.

def lotkavolterra(t, z, a, b, c, d):
    x, y = z
    return [a*x - b*x*y, -c*y + d*x*y]
# ...

# We pass in the parameter values a=1.5, b=1, c=3 and d=1 with the `args`
# argument.

sol = solve_ivp(lotkavolterra, [0, 15], [10, 5], args=(1.5, 1, 3, 1),
                dense_output=True)

# Compute a dense solution and plot it.

t = np.linspace(0, 15, 300)
z = sol.sol(t)
import matplotlib.pyplot as plt
plt.plot(t, z.T)
plt.xlabel('t')
plt.legend(['x', 'y'], shadow=True)
plt.title('Lotka-Volterra System')
plt.show()
