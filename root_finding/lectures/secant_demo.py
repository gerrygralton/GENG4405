# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 18/07/2022

import numpy as np
import matplotlib.pyplot as plt

# Define the equation for the
# natural freuqencies of a clamped beam.
# Secant method does not require an analytic derivative
def func(x):
    return np.cos(x) * np.cosh(x) + 1

# Define the equation for the terminal velocity example
def func(x):
    g = 9.81
    M = 0.002
    return 1.35e-5 * x**1.5 + 1.18e-5 * x**2 - g * M

# Secant method requires two inital guesses
x_0 = 1.2
x_1 = 1.3

# We've got enough values to start but we'll do the first iteration outside of the loop
# This is so we can calculate error before we start
x_2 = x_1 - func(x_1) * (x_1 - x_0) / (func(x_1) - func(x_0))
error = np.abs( x_2 - x_1 ) / x_2

# We'll start a plot too, so we can see it converge
x = np.linspace(x_0, x_2 , num=20)    # Generate a list with every number from 0 to 12 in steps of 0.1
plt.plot(x, func(x))
plt.grid(True)
# plt.show()

# Time for looping
tol = 1e-4
count = 1

while (error > tol):
    # Visualise each step
    plt.plot([x_1, x_2], [func(x_1), 0], '--', color='r')
    plt.plot([x_1, x_2], [func(x_1), func(x_2)], 'o', color='r')
    plt.pause(1)

    # Update all values in the loop
    x_0 = x_1
    x_1 = x_2
    x_2 = x_1 - func(x_1) * (x_1 - x_0) / (func(x_1) - func(x_0))
    error = np.abs(x_2 - x_1) / x_2

    count += 1

    if (count > 20):
        print("Excessive iterations (iter = 20)")
        break

print("Root is at %.3f" % x_2)
print("Root found in %i iterations" % count)
plt.show()
