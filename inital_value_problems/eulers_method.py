# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 09/02/2022

import numpy as np
import matplotlib.pyplot as plt

# Define an ODE describing change in concentration
def dc(c):
    return -0.06 * c

# Set up some stepping parameters
totaltime = 7
steps = 20
h = totaltime / steps   # Step width
c_old = 1e7

# Create a 2D array with slots for each step and the concentation at that step
solution = np.zeros([steps+1, 2])

solution[0,0] = 0
solution[0,1] = c_old

# Time to do some stepping
# Don't forget that python indexs from 0
for i in range(1, steps+1):
    c_new = c_old + dc(c_old)*h
    solution[i, 0] = i * h  # New time value
    solution[i, 1] = c_new  # New concentration value

    #Update the variables so we can do the next loop
    c_old = c_new


# If you've got data, you should always plot it!
plt.plot(solution[:, 0], solution[:, 1])
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.show()
