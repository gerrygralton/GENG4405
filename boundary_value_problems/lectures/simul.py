# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 20/07/2022
#
# simul.py plots a trajectory of a cannon ball using
# initial conditions computed using the shooting method

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from find_root import find_root
from position_error import position_error
from derivatives import derivatives

t0 = 0
tf = 50
y0 = np.array([0, 0])
yf = np.array([10000, 500])	# Target 10000m away on 500m mountain

tol = 1e-3	# Tolerance required

# Plot the trajectory
plt.plot(yf[0], yf[1], 'o')
# plt.show()

v = find_root(position_error, np.array([200, 255]), np.array([1, 1]), tol)
sol = solve_ivp(derivatives, np.array([t0, tf]), np.array([y0[0], y0[1], v[0], v[1]]))

plt.plot(sol.y[0, :], sol.y[1, :])
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
