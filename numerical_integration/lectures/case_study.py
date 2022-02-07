# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 07/02/2022

# First thing to do is import a few extra modules
import numpy                        # For maths operations with arrays etc
import matplotlib.pyplot as plt     # For plotting

# The function that needs integrating looks like this
def func(u):
    return 2000 * u / (8.1 * u ** 2 + 1200)

# Now we need to define the some variables for the Trapezoid method:
a = 0                   # Lower integration bound
b = 30                  # Upper integration bound
n = 5                   # Number of partitions
h = (b - a) / n         # Width of each partition

# Initialise an array for use with looping
times = numpy.zeros(n+1)
speeds = numpy.zeros(n+1)

# Now we need to calculate the function values at all points
# We can do that with a `for` loop
# Don't forget that range() doesn't include the last number
for i in range(n+1):
    times[i] = a + i * h
    speeds[i] = func(times[i])

midsum = sum(speeds[range(1, n)])

# Compute the integral:
distance = h/2 * (speeds[0] + 2 * midsum + speeds[n])

# Then we can plot our data
plt.plot(times, speeds, 'darkblue', label="Trapezoid approximation")

for i in range(n+1):
    plt.plot([times[i], times[i]], [0, speeds[i]],
             'darkblue')                                    # Vertical lines

plt.plot(numpy.arange(a, b, h/100),
         [func(point) for point in numpy.arange(a, b, h/100)],
         'red', label="Real curve")                         # Accurate curve

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend(loc="upper right")
plt.show()

print("Using Trapezoid rule the car travelled: %.2f metres" % distance)
