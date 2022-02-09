# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 07/02/2022

# First thing to do is import the 'math' module so we can do operations
# like take logs
import math

# Let's start with a function that we need to integrate
def func(t):
    return 2000 * math.log(140000/(140000-2100*t)) - 9.8*t

# Now we need to define the values of the variables to use Simpson's method:
a = 8                   # Lower integration bound
b = 30                  # Upper integration bound
n = 20                  # Number of partitions
h = (b - a) / n         # Width of each partition

# Initialise values for use with looping
oddsum = 0
evensum = 0

# Now we need to calculate the function values at the interior points
# We can do that with a `for` loop
# Don't forget that range() doesn't include the last number
for i in range(1, n):
    x_i = a + i * h
    if (i % 2 == 0):
        evensum += func(x_i)
    else:
        oddsum += func(x_i)

# Compute the integral:
integral = h/3 * (func(a) + 4 * oddsum + 2 * evensum + func(b))

print("Using Simpson's rule the integral is: ")
print(integral)
