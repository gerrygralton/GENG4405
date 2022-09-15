# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 30/06/2022

def trapezoid(f_name: str, a, b, n: int):

    # trapezoid() integrates function f_name in the interval [a b]
    # using trapezoidal rule (on n intervals) and
    # illustrates graphically the procedure.
    # The function is called as:
    # trapezoid(f_name,a,b,n)

    h = (b - a) / n     # Width of each partition

    midsum = 0          # Initialise values for use with looping

    # Now we need to calculate the function values at the interior points
    # We can do that with a `for` loop
    # Don't forget that range() doesn't include the last number

    for i in range(1, n):
        x_i = a + i * h
        midsum += f_name(x_i)

    # Compute the integral:
    return h/2 * (f_name(a) + 2 * midsum + f_name(b))
