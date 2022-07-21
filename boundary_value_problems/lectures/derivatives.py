# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 20/07/2022
#
# derivatives() returns the values of the derivatives as a four ele-
# ment column vector for the cannon ball trajectory case study
# using the given expressions for the acceleration.
# That is,
#        dY = (vel_x,vel_y,acc_x,acc_y)
# The aerodynamical drag is assumed to be
# proportional to the square of velocity.
# A constant gravitational acceleration is assumed, with
# ax=0 and ay = -9.81.  The input t is a scalar and y is a
# four element column vector containing (x,y,vel_x,vel_y).  The
# use is
#          dY = derivatives(t,Y)

import numpy as np

def derivatives(t, Y):
    m = 0.5     # Mass
    c = 1e-4    # Aerodynamic drag
    absv = np.sqrt(Y[2]**2 + Y[3]**2)
    return [Y[2], Y[3], -c / m * Y[2] *absv, -9.81 - c / m * Y[3] * absv]
