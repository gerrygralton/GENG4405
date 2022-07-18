# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 18/07/2022

import numpy as np
import matplotlib.pyplot as plt

# Define the equation and analytic derivative for the
# natural freuqencies of the clamped beam
def func(x):
    return np.cos(x) * np.cosh(x) + 1

def func_der(x):
    return -(np.sin(x)) * np.cosh(x) + np.cos(x) * np.sinh(x)

# Define the equation and analytic derivative for the
# terminal velocity example
# def func(x):
#     g = 9.81
#     M = 0.002
#     return 1.35e-5 * x**1.5 + 1.18e-5 * x**2 - g * M
#
#     def func_der(x):
#         return 2.025e-5 * x**(0.5) + 2.36e-5 * x

# Newton-Raphson requires us to take a guess at the root
x_old = 1.2

# We've got enough values to start but we'll do the first iteration outside of the loop
# This is so we can calculate error before we start
value = func(x_old)
deriv = func_der(x_old)
dx = - value / deriv
x_new = x_old + dx
error = np.abs( x_new-x_old ) / x_new

# We'll start a plot too, so we can see it converge
x = np.linspace(x_old - 2, x_old + 2 , num=20)
plt.plot(x, func(x))
plt.grid(True)
# plt.show()

# Time for looping
tol = 1e-4
count = 1

while (error > tol):
    # Visualise each step
    plt.plot([x_old, x_old + dx], [value, 0], '--', color='r')
    plt.plot([x_old, x_old + dx], [value, func(x_new)], 'o', color='r')
    plt.pause(1)

    # Update all values in the loop
    x_old = x_new
    value = func(x_old)
    deriv = func_der(x_old)
    dx = - value / deriv
    x_new = x_old + dx
    error = np.abs(x_new - x_old) / x_new

    count += 1

    if (count > 20):
        print("Excessive iterations (iter = 20)")
        break
    if ( np.abs( deriv ) < tol):
        print("small derivative, method diverging")
        break



print("Root is at %.3f" % x_new)
print("Root found in %i iterations" % count)
plt.show()
