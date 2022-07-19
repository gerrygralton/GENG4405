# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 19/07/2022

import numpy as np

def dydt(t, y):
    G = 6.67e-11
    ME = 5.97e24
    X = y[0:2]
    V = y[2:4]
    r = np.sqrt(np.sum(X**2))

    dVdt = -G * ME * X / (r**3)

    return np.array([V[0], V[1], dVdt[0], dVdt[1]])
