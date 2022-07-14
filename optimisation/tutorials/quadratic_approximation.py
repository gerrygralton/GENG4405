# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 07/02/2022

# First thing is to import useful modules
import numpy as np
import matplotlib.pyplot as plt

# The function we are looking to optimise:
def func(x):
    return (x**2 - 4)**2 / 8 - 1

# Define a function the approximates the quadratic root of three point
def find_quad_root(function, x_l, x_m, x_u):
    f_l = function(x_l)
    f_m = function(x_m)
    f_u = function(x_u)

    return (f_l*(x_m**2 - x_u**2) + f_m*(x_u**2-x_l**2) + f_u*(x_l**2-x_m**2))\
        / (2*(f_l * (x_m - x_u) + f_m*(x_u-x_l) + f_u * (x_l-x_m)))

# We have data so let's have a look at it before we do anything else
x = np.arange(0, 3, 0.1)    # Generate a list with every number from 0 to 3 in steps of 0.1
plt.plot(x, func(x))
# plt.show()

# OK, set some bounds for the area to search in
x_lower = 0
x_upper = 3

# Determine the intermediate point and evaluate the function there
x_middle = (x_lower + x_upper) / 2
f_middle = func(x_middle)

# Do the first iteration outside of the loop so we can estimate initial error
x_new = find_quad_root(func, x_lower, x_middle, x_upper)
f_new = func(x_new)

# Now we need to do some iterating to narrow down the area
# Intialise some loop variables
tol = 0.05
error = abs(x_new - x_middle)
count = 1

# Now, iterate!
while (error > tol and count < 100):
    if (x_new > x_lower and x_new < x_middle):
        if (f_new < f_middle):
            x_upper = x_middle
            x_middle = x_new
        else:
            x_lower = x_new
    else:
        if (f_new < f_middle):
            x_lower = x_middle
            x_middle = x_new
        else:
            x_upper = x_new

    # Update all our variables (check the order!)
    f_middle = func(x_middle)

    x_new = find_quad_root(func, x_lower, x_middle, x_upper)
    f_new = func(x_new)

    error = abs(x_new - x_middle)
    count += 1

print("Minima is at: %3.4f" % x_new)
print("Minima found in %i iterations" % count)
