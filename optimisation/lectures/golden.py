# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 15/07/2022
#
# golden(a,b,small,fnc) starts with an interval [a,b], that
# is known to contain a minimum of the function contained
# in the function (string constant fnc) and successively
# reduces the size of the interval by the golden search
# method until the interval is less than small.  It then
# returns the center of that interval as the position of
# the minimum.  The use is r = golden(a,b,small,fnc).

import math

def golden(x_lower, x_upper, small, func, data):

    # Determine the intermediate points
    gamma = 1 - (math.sqrt(5) - 1) * 0.5

    d = x_upper - x_lower
    x_2 = x_lower + gamma * d
    x_3 = x_upper - gamma * d

    # Now we need to do some iterating to narrow down the area
    # Intialise some loop variables
    error = x_upper - x_lower
    count = 0

    # Now, iterate!
    while (error > small and count < 100):
        if (func(x_2, data) > func(x_3, data)):
            x_lower = x_2
            h = x_upper - x_lower
            x_2 = x_3
            x_3 = x_upper - gamma * h
        else:
            x_upper = x_3
            h = x_upper - x_lower
            x_3 = x_2
            x_2 = x_lower + gamma * h

        error = x_upper - x_lower
        count += 1

    return 0.5 * (x_2 + x_3)
