# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 07/02/2022

# First thing is to import useful modules
import math
import numpy as np
import matplotlib.pyplot as plt

# The function we are looking to optimise:
def func(x):
    return (x**2 - 4)**2 / 8 - 1

def recursive_golden(function, x_l, x_2, x_3, x_u, count, tol):
    count += 1
    error = x_u - x_l

    if (error < tol or count > 100):
        sol = (x_u + x_l) / 2
    else:
        r = (math.sqrt(5) - 1) / 2

        if (func(x_2) > func(x_3)):
            x_l = x_2
            h = x_u - x_l
            x_2 = x_3
            x_3 = x_u - (1-r) * h
        else:
            x_u = x_3
            h = x_u - x_l
            x_3 = x_2
            x_2 = x_l + (1-r) * h

        sol, count = recursive_golden(func, x_l, x_2, x_3, x_u, count, tol)
    return sol, count

# We have data so let's have a look at it before we do anything else
x = np.arange(0, 3, 0.1)    # Generate a list with every number from 0 to 3 in steps of 0.1
plt.plot(x, func(x))
# plt.show()

# OK, set some bounds for the area to search over
x_lower = 0
x_upper = 3

# Determine the intermediate points
r = (math.sqrt(5) - 1) / 2
h = x_upper - x_lower
x_2 = x_lower + (1-r) * h
x_3 = x_upper - (1-r) * h

# Plot it to check it makes sense
plt.scatter([x_2, x_3], [func(x_2), func(x_3)], color='r', label="Golden ratio points")
plt.legend()
# plt.show()

# Now we need to do some iterating to narrow down the area
# Intialise some loop variables
tol = 0.05
count = 0

# Now, go down the rabbit hole recursively!
solution, count = recursive_golden(func, x_lower, x_2, x_3, x_upper, count, tol)

print("Minima is at: %3.4f" % solution)
print("Minima found in %i iterations" % count)
