# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 30/06/2022

import numpy as np
import matplotlib.pyplot as plt

def trapezoid(f_name, a, b, n: int):
#   trapezoid() integrates function f_name in the interval [a b]
#   using trapezoidal rule (on n intervals) and
#   illustrates graphically the procedure.
#   The function is called as:
#       trapezoid(f_name,a,b,n)
#   where f_name is the name of the function to integrate,
#   a and b are the integral bounds and n is the number of partitions.
#
#   To import this into an ineractive python environment,
#   ensure the working directory contains this file, type
#       `from trapezoid import trapezoid`
#   and then call the function as outlined above.
# ==========================================================
    h = (b - a) / n     # Width of each partition

    # Now we need to calculate the function values at the interior points
    # We can do that with a `for` loop
    # Don't forget that range() doesn't include the last number

    x = np.arange(a, b+h, h)
    y = np.zeros(n+1)

    for i in range(n+1):
        y[i] = f_name(x[i])

    # Then we can plot our data
    plt.plot(x, y, 'darkblue', label="Trapezoid approximation")

    for i in range(n+1):
        plt.plot([x[i], x[i]], [0, y[i]], 'darkblue')   # Vertical lines

    plt.plot(np.arange(a, b, h/100),
             [f_name(point) for point in np.arange(a, b, h/100)],
             'red', label="Real curve")                         # Accurate curve

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="upper right")
    plt.show()

    # Compute the integral:
    return h/2 * (f_name(a) + 2 * np.sum(y[range(1, n)]) + f_name(b))
