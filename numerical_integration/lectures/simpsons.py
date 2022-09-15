# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 30/06/2022


def simpsons(f_name: str, a, b, k: int):
# simpsons() will integrate the function f_name over the interval
#   a<x<b using n = 2^k panels and return the intergral.
#   The use is:
#        s = simpsons(f_name,a,b,k)
# ==========================================================
    if k<=0:
        error("k must be a positive integer")
# ==========================================================
    n = 2**k # Number of partitions
    h = (b - a) / n

    for i in range(1, n):
        x_i = a + i * h
        if (i % 2 == 0):
            evensum += f_name(x_i)
        else:
            oddsum += f_name(x_i)

    return h/3 * (f_name(a) + 4 * oddsum + 2 * evensum + f_name(b))
