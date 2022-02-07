# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 07/02/2022

# First thing to do is import the 'math' module so we can do operations
# like take logs
import math

# Let's start with a function that we need to integrate
def func(t):
    return 2000 * math.log(140000/(140000-2100*t)) - 9.8*t

# Now we need to define some variables used for Gaussian quadrature:
# First are the locations and weights of the gauss points.
# Decide on how many to use then grab them from wikipedia.
x_gauss = [-math.sqrt(3.0 / 5.0), 0.0, math.sqrt(3.0 / 5.0)]
weights_gauss = [5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0]

a = 8               # Lower integration bound
b = 30              # Upper integration bound
n = len(x_gauss)    # Number of Gauss points you want to use

# Initialise values for use with looping
pointsum = 0

# Now we need to calculate the function values at each gauss point
# We can do that with a `for` loop
# Don't forget that range() doesn't include the last number
for i in range(n):
    x_real = (b - a) / 2 * x_gauss[i] + (b + a) / 2 # Shift the quadrature point
    qpoint = weights_gauss[i] * func(x_real)
    pointsum += qpoint

# Compute the integral:
integral = (b - a) / 2 * pointsum

print("Using Gaussian quadrature the integral is: ")
print(integral)
