# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 18/07/2022
#
# function stepping refines interval in which function f_name changes sign
# x0 and x1 define the initial interval. x0 must be smaller that x1.
# Use is: stepping(f_name, x0,x1)

def stepping(func, x_0, x_1)

    if ( func(x_0) * func(x_1) > 0 ):
        print("No root (or even number of roots) in interval")
        return

    dx = (x_1 - x_0) / 50
    x = x_0 + dx

    while ( x < x_1 ):
        if ( func(x) * func(x_0) <= 0 ):
            x_left = x - dx
            x_right = x
            print("Interval containing root is [%.2f - %.2f]" % (x_left, x_right))
            break
        x = x + dx
