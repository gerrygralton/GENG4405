# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 18/07/2022
#
# bisection() finds root of func() in the interval [a c] and
# illustrates graphically the procedure in the plot between xmin and xmax.
# n_points points are plotted. The function is called as:
# bisection(func, x_lower, x_upper)

import numpy as np
import matplotlib.pyplot as plt

def bisection(func, x_lower, x_upper):

    # Check that the bounds contain a root
    if ( func(x_lower) * func(x_upper) > 0 ):
        print("No roots, or even number of roots in the interval")
        return

    # Set up a plot for visualisation
    x = np.linspace(x_lower, x_upper, 100)
    plt.plot(x, func(x))
    plt.plot([x_lower, x_upper], [0, 0])
    plt.plot([x_lower, x_lower], [0, func(x_lower)], '--', color='r')
    plt.plot([x_upper, x_upper], [0, func(x_upper)], '--', color='r')
    plt.plot([x_lower, x_upper], [func(x_lower), func(x_upper)], 'o', color='r')

    # Now that we've got a range with a root in it, we can use the bisection method
    count = 1
    count_limit = 30
    tol = 1e-4
    x_middle = (x_upper + x_lower) / 2
    error = x_upper - x_lower

    # We're going to use a for loop to do this and break once tolerance is met
    # What might be a better way to do this?
    while True:
        x_middle = (x_upper + x_lower) / 2

        if (func(x_lower) * func(x_middle) < 0):
            x_upper = x_middle
        else:
            x_lower = x_middle

        error = x_upper - x_lower

        plt.plot([x_middle, x_middle], [0, func(x_middle)], '--', color='r')
        plt.plot(x_middle, func(x_middle), 'o', color='r')
        plt.pause(1)

        if (error < tol):
            print("Tolerance is satisfied!")
            break
        if (count > count_limit):
            print("Iteration limit exceeded")
            break
        
        count += 1

    plt.show()
    print("Root at %.3f" % x_middle)
    print("Root found in %i iterations" % count)
    return x_middle
