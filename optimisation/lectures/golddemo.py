# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 15/07/2022
#
# Script file golddemo.py demonstrates the golden search method
# applied to the function for the range of a rocket as a
# function of orientation angle of the rockets.

import numpy as np
import matplotlib.pyplot as plt

from golden import golden   # Import golden search function from golden.py
from thrust import thrust    # Import thrust search function from thrust.py

ve = 1500       # Exhaust velocity
omega=0.125     # Fuel mass/total mass
tc = 6          # Time of cut-off
data = [ve, omega, tc]
small = 3e-2

print(""" The rocket parameters are:
    ve =    %i m/s      exhaust velocity
    tc =    %i s        time of cut-off
    Omega = %.3f        fuel mass/total mass
The range is computed for a variety of orientation
angles.  It is presumed that the maximum range is
obtained for an angle between 20 and 70 degrees.
The golden mean method reduces this interval by a
factor of  0.6180... in each step.  This factor is
known as the golden mean.""" % (ve, tc, omega))

a = 20
b = 70
degs = np.arange(a, b)
theta = degs * np.pi / 180
thrusts = -thrust(theta, data)
plt.plot(degs, thrusts)
# plt.show()

A = a * np.pi/180       # Convert to radians
B = b * np.pi/180

theta_min = golden(A, B, 1e-5, thrust, data)    # Find optimal angle
deg_min = 180 * theta_min / np.pi
plt.plot([deg_min, deg_min], [0, -thrust(theta_min, data)], '--')
# plt.show()

if (A > B ):
    x = np.array([B, 0, 0, A])
else:
    x = np.array([A, 0, 0, B])

# Determine the intermediate points
beta = (np.sqrt(5) - 1) * 0.5
gamma = 1 - beta

d = x[3] - x[0]
x[1] = x[0] + gamma * d
x[2] = x[3] - gamma * d
thrusts = thrust(x, data)

# Now we need to do some iterating to narrow down the area
# Intialise some loop variables
count = 0

# Plotting constants
Ly = 7000
Lx = 50
ymin = 0
xmin = 20

# Now, iterate!
while (d > small and count < 100):
    degs = 180 * x / np.pi              # Plotting stuff
    plt.plot(degs, -thrusts, 'o')
    height = np.ones(4) + (count * Ly/10)
    plt.plot(degs, ymin + height, marker='+')
    plt.plot([degs[0], degs[0]], [ymin + height[0], -thrusts[0]], ':')
    plt.plot([degs[3], degs[3]], [ymin + height[0], -thrusts[3]], ':')
    plt.pause(1)

    d = d * beta    # Do the actual golden search
    if (thrust(x[1], data) > thrust(x[2], data)):
        x = np.array([x[1], x[2], x[3]-gamma*d, x[3]])
        thrusts = np.array([thrusts[1], thrusts[2], thrust(x[2], data), thrusts[3]])
    else:
        x = np.array([x[0], x[0]+gamma*d, x[1], x[2]])
        thrusts = np.array([thrusts[0], thrust(x[1], data), thrusts[1], thrusts[2]])

    count += 1

    
plt.title("Golden mean method of finding extrema")
plt.xlabel("Theta (deg)")
plt.ylabel("Range (m)")
plt.show()

r =  0.5 * (x[1] + x[2])
angle = 180 * r / np.pi

print("The optimum angle is %.2f degrees." % angle)
print("The maximum range is %.2f metres." % -thrust(theta_min, data))
