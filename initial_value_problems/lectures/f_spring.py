# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 19/07/2022
#
# f_spring(t,y) gives the right side of matrix equation for mass, spring
# dumper system from Nakamura, Example 10.7, p.337
# M is a mass, B is a dumping coefficient, k is a spring constant
# g is the gravity acceleration

import numpy as np

def f_spring(t, y):
    M = 10
    B = 50
    k = 200

    return np.array( [y[1], -B / M * np.abs(y[1]) * y[1] - k / M * y[0] ])
