# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 09/02/2022

'''
This function is a standard implementation of Euler's method but involves a
slight twist in that we integrate two functions at the same time
Arguments:
    func1 - the first function to be integrated
    func2 - the second function to be integrated
    steps - 1D array of each evaluation point
    u0 - inital condition
    w0 - initial condition
'''

import numpy as np

def eulers(func1, func2, steps, u0, w0):
    solution = np.zeros([len(steps), 3])
    solution[:, 0] = steps
    solution[0, 1] = u0
    solution[0, 2] = w0

    u_old = u0
    w_old = w0

    for i in range(1, len(steps)):
        h = steps[i] - steps[i-1]
        r = steps[i]

        u_new = u_old + func1(r, u_old, w_old) * h
        w_new = w_old + func2(r, u_old, w_old) * h

        solution[i, 1] = u_new
        solution[i, 2] = w_new

        u_old = u_new
        w_old = w_new

    return solution
