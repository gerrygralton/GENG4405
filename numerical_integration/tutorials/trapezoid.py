# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 07/02/2022

# First thing to do is import the 'math' module so we can do operations
# like take logs
import math

# Let's start with a function that we need to integrate
def func(t):
    return 2000 * math.log(140000/(140000-2100*t)) - 9.8*t

# Now we need to define the some variables for the Trapezoid method:
a = 8                   # Lower integration bound
b = 30                  # Upper integration bound
n = 20                  # Number of partitions
h = (b - a) / n         # Width of each partition

# Initialise values for use with looping
midsum = 0

# Now we need to calculate the function values at the interior points
# We can do that with a `for` loop
# Don't forget that range() doesn't include the last number

for i in range(1, n):
    x_i = a + i * h
    midsum += func(x_i)

# Compute the integral:
integral = h/2 * (func(a) + 2 * midsum + func(b))

print("Using Trapezoid rule the integral is: ")
print(integral)
