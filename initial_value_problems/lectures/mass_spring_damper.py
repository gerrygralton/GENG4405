# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 19/07/2022

import numpy as np
import matplotlib.pyplot as plt

from euler_vector import euler_vector
from f_spring import f_spring

# This is the equation that solves the dumper system with mass M,
# dumping coefficient B and spring constant k.
#
# For the time t, the input values are in the range of t's [a<=t<=b],
# with a being the initial time and b the final one.

a = 0
b = 15

# The initial values y0, for position and velocity are given as a vector
y0 = np.array([0, 0.02])

N = 10000   # Number of steps

# Solve the IVP
y, steps = euler_vector(a, b, y0, N, f_spring)

# And plot the results
plt.plot(steps, y[:,0], label="Position")
plt.plot(steps, y[:,1], label="Velocity")
plt.legend()
plt.show()
