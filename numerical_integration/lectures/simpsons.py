# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 30/06/2022

import numpy as np
import matplotlib.pyplot as plt

def simpsons(f_name, a, b, k: int):
#   simpsons() will integrate the function f_name over the interval
#   a<x<b using n = 2^k panels, plot it and return the intergral.
#   The use is:
#        s = simpsons(f_name,a,b,k)
#   where f_name is the name of the function to integrate,
#   a and b are the integral bounds and 2^k is the number of partitions.
#
#   To import this into an ineractive python environment,
#   ensure the working directory contains this file, type
#       `from simpsons import all`
#   and then call the function as outlined above.
# ==========================================================
    if k<=0:
        error("k must be a positive integer")
# ==========================================================
    n = 2**k # Number of partitions
    h = (b - a) / n

    evensum = 0
    oddsum = 0

    x = np.zeros(n-1)
    y = np.zeros(n-1)

    for i in range(1, n):
        x[i-1] = a + (i) * h
        y[i-1] = f_name(x[i-1])

        if (i % 2 == 0):
            evensum += y[i-1]
        else:
            oddsum += y[i-1]

    # Then we can plot our data
    for i in range(n-1):
        plt.plot([x[i], x[i]], [0, y[i]], 'darkblue')   # Vertical lines

    plt.plot(np.arange(a, b, h/100),
             [f_name(point) for point in np.arange(a, b, h/100)],
             'red', label="Real curve")                         # Accurate curve

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="upper right")
    plt.show()

    return h/3 * (f_name(a) + 4 * oddsum + 2 * evensum + f_name(b))
