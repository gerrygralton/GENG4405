# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 19/07/2022

import numpy as np

# euler_vector() solves a system of first order differential equations
# y' = fnc(t,y) by a simple stepping procedure using
# the first two terms of a Taylor expansion of the
# function y(t).  The function contained in the string
# variable func must expect a vector with time and the VoI
# The program is not suitable
# for realistic solutions of a differential equation.
# The input values are the range of t's [a<=t<=b], the
# initial value of y, [y0] (column vector), the number of steps [N].  A
# 3xN matrix of computed values is returned in Y.
# The use is Y = euler_vector(a,b,y0,N,fnc)

def euler_vector(a, b, y0, n, func):
    dt = (b - a) / n
    steps = np.linspace(a, b, n)
    y = np.zeros([n, len(y0)])
    y[0, :] = y0

    for i in range(n-1):
        y[i+1, :] = y[i, :] + dt * func(steps[i], y[i, :])

    return y, steps
