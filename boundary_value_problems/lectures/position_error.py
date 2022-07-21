# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 20/07/2022
#
# position_error() uses estimates for the initial velocity contained
# in the vector v to compute the complete trajectory
# of the cannonball.  The values of the (x,y) coordinates at
# the END of the interval are then compared with the actual
# end conditions and the difference is returned in the two
# element vector dy.
#
# If dy = 0, the values in v corresponding to the desired
# missing initial velocity have been found.
#
#  The use is
# 		 dy = PositionError(v).

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from derivatives import derivatives

def position_error(v):
    t0 = 0
    tf = 50
    pos0 = np.array([0, 0])
    posf = np.array([10000, 500])   # target 10000 m away
                                    # on a 500 m high mountain

    proj0 = [pos0[0], pos0[1], v[0], v[1]]
    sol = solve_ivp(derivatives, (t0, tf), proj0, method="RK45")

    return posf - sol.y[0:2, -1]
