# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 09/02/2022

import numpy as np                  # For maths operations with arrays etc
import matplotlib.pyplot as plt     # For plotting

# OK, let's define our function
def func(x):
    return -0.019 * x**3 + 0.435 * x**2 - 3.145 * x + 6.885

def func_der(x):
    return -0.057 * x**2 + 0.87 * x - 3.145

# The first thing to do, in any situation, is to visually inspect the data
x = np.arange(0, 12, 0.1)    # Generate a list with every number from 0 to 12 in steps of 0.1
plt.plot(x, func(x), label="Function")
plt.plot(x, func_der(x), label="Derivative")
plt.grid(True)
plt.legend()
# plt.show()

# Newton-Raphson requires us to take a punt at the root location
x_old = 3.5

# We've got enough values to start but we'll do the first iteration outside of the loop
# This is so we can calculate error before we start
x_new = x_old - func(x_old) / func_der(x_old)
# we'll store error in a list so we can see how the error converges afterwards
error = [(x_new - x_old) / x_new]

# Time for looping
tol = 1e-4
count = 1
while (error[-1] > tol):
    x_old = x_new
    x_new = x_old - func(x_old) / func_der(x_old)
    error.append((x_new - x_old) / x_new)

    count += 1

    if (count > 1000):
        break

print("Root is at %3.4f" % x_new)
print("Root found in %i iterations" % count)

plt.clf()  # Clear the last plot
plt.plot(error)
plt.grid(True)
# plt.show()
