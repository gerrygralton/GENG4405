# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 19/07/2022

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from euler_vector import euler_vector
from dydt import dydt

# Initialise the parameters
G = 6.672e-11
M = 5.97e24
R = 4.223e7
v0 = 0.5 * 3071
y0 = np.array([-R, 0, 0, v0])
N = 10000
t0 = 0
T = (60*60*24)*5

# Next, the orbit is computed by integrating four simultaneous 1st
# order equations for (x', y', vx', vy') respectively.  These
# derivatives must be returned by the function dydt().

results = solve_ivp(dydt, (t0, T), y0, method="RK45", rtol=1e-4, atol=1e-4);

# The x,y coordinates of the orbit are now contained in y(:, 1), y(:, 1).
# This orbit is then plotted.

plt.plot(0,0, 'o')
plt.plot(results.y[0, :], results.y[1, :])
plt.show()
