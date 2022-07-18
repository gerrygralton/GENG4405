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

# The secant method requires two initial guesses so let's make some
x_0 = 2
x_1 = 2.5

# We've got enough values to start but we'll do the first iteration outside of the loop
# This is so we can calculate error before we start
x_2 = x_1 - func(x_1) * (x_1 - x_0) / (func(x_1) - func(x_0))
# we'll store error in a list so we can see how the error converges afterwards
error = [np.abs(x_2 - x_1) / x_2]

# Time for looping
tol = 1e-4
count = 1
while (error[-1] > tol):
    x_0 = x_1
    x_1 = x_2
    x_2 = x_1 - func(x_1) * (x_1 - x_0) / (func(x_1) - func(x_0))
    error.append(np.abs(x_2 - x_1) / x_2)

    count += 1

print("Root is at %3.4f" % x_2)
print("Root found in %i iterations" % count)

plt.clf()  # Clear the last plot
plt.plot(error)
plt.grid(True)
plt.show()
