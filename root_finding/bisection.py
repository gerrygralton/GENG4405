# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 09/02/2022

import numpy as np                  # For maths operations with arrays etc
import matplotlib.pyplot as plt     # For plotting

# OK, let's define our function
def func(x):
    return -0.019 * x**3 + 0.435 * x**2 - 3.145 * x + 6.885

# The first thing to do is have a look at our data
x = np.arange(0, 12, 0.1)    # Generate a list with every number from 0 to 12 in steps of 0.1
plt.plot(x, func(x))
plt.grid(True)
# plt.show()

# OK, so we can see the roots visually but how can we find it numerically?
# Let's pick two points which definitely contain the roots
x_lower = 3
x_upper = 4.5

plt.scatter([x_lower, x_upper], [func(x_lower), func(x_upper)], color='r')
# plt.show()

# Now that we've got a range with a root in it, we can use the bisection method
N = 100
tol = 1e-4
error = x_upper - x_lower

# We're going to use a for loop to do this and break once tolerance is met
# What might be a better way to do this?
for count in range(N):
    x_middle = (x_upper + x_lower) / 2

    if (func(x_lower) * func(x_middle) < 0):
        x_upper = x_middle
    else:
        x_lower = x_middle

    error = x_upper - x_lower

    if (error < tol):
        break

print("Root is at %3.4f" % ((x_upper + x_lower)/2))
print("Root found in %i iterations" % count)
