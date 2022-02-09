# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 09/02/2022

import numpy as np
import matplotlib.pyplot as plt

# Define an ODE describing a temperature model
def dx(t, x):
    return -2.2067e-12 * (x**4 - 81e8)

# Set up some stepping parameters
totaltime = 480
h = 120                         # Step width
steps = round(totaltime / h)    # round() is used to make steps steps is a whole number

# Set up the initial state
t_old = 0
x_old = 1200

# Create a 2D array with slots for each step and the concentation at that step
solution = np.zeros([steps+1, 2])

solution[0,0] = t_old   # Put time in the first column
solution[0,1] = x_old   # Put temperature in the second column

# Time to do some stepping
# Don't forget that python indexs from 0
for i in range(1, steps+1):
    k1 = dx(t_old, x_old)
    k2 = dx(t_old + h/2, x_old + k1 * h/2)
    k3 = dx(t_old + h/2, x_old + k2 * h/2)
    k4 = dx(t_old + h, x_old + k3 * h)
    x_new = x_old + (k1 + 2*k2 + 2*k3 + k4) * h / 6
    t_new = t_old + h

    # Store the solution
    solution[i, 0] = t_new
    solution[i, 1] = x_new

    #Update the variables so we can do the next loop
    t_old = t_new
    x_old = x_new

# Now we have the data, we definitely need to plot it
plt.plot(solution[:, 0], solution[:, 1])
plt.xlabel("Time (s)")
plt.ylabel("Temperature (K)")
plt.show()
