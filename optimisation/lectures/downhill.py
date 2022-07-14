# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 14/07/2022

# Downhill evaluates the function, func, at two points,
# x0, x1 (scalars) and then
# follows the function downhill until a minimum is attained.
# It returns two x values in a,b that bracket the minimum.
# The range of the search is limited by specifying the maximum
# distance as a multiple of the distance abs(x1-x0) and is
# entered as max.  The function must accept column vector input.
# The use is
# [a,b] = downhill(fnc, x0, x1, max)

def downhill(f_name: str, x0: int, x1: int, max: int):
    x = [x0, 0.5 * (x0 + x1), x1]
    f = [f_name(x[0]), f_name(x[1]), f_name(x[2])]

    if (f[0] > f[1] and f[2] > f[1]):
        return [x[0], x[2]]

    if ( f[0] < f[1] ):
        x.reverse()
        f.reverse()

    count = 0

    while (f[2] <= f[1]):
        if ( f[0] <= f[1] ):
            print("Interval contains local max between %.2f and %.2f" % (x[1], x[2]))
            return [x[0], x[2]]

        b = 2*x[2] - x[1]
        x = [x[1], x[2], b]
        f = [f[1], f[2], f_name(b)]

        count = count + 1

        if ((abs(x[2] - x0) / abs(x1 - x0) > max) or (count > 100)):
            print("Out of range")
            print("No minimum found between %3.4f and %3.4f" % (x0, x1))
            return [x[2], x[2]]

    if ( x[2] < x[0] ):
        x.reverse()

    return [x[0], x[2]]
