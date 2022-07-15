# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 15/07/2022
#
# thrust(th) computes the range of a constant thrust rocket.
# The exhaust relative velocity (ve), the original
# fuel-to-mass ratio (Omega), the time of engine
# cut-off in seconds (tc) must be specified in the calling
# program and declared as global.  The range is com-
# puted for a collection of orientation angles con-
# tained in the column vector theta and is returned as a vector
# of values.  The angle theta is in radians.
# The use is
#           R = thrust(theta)
# The value returned is the negative of the range, so
# that if finding the minimum of this function determines
# the maximum range and optimum angle theta.

import numpy as np

def thrust(theta, data):

    ve = data[0]
    omega = data[1]
    tc = data[2]

    g = 9.8
    tau = tc/omega
    u = tc/tau
    q = np.log(1-u)
    vxc = -q * ve * np.cos(theta)
    vyc = -q * ve * np.sin(theta) - g * tc
    xc = ve * tau * np.cos(theta) * ( u + (1-u) * q)
    yc = ve * tau * np.sin(theta) * ( u + (1-u) * q) - 0.5 * g * tc**2
    arg = 2 * g * yc / (vyc**2) + 1
    return -1 * ( xc + 2 * ( vxc * vyc / g ) *( 1 + np.sqrt(arg)))
