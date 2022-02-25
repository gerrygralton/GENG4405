# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 10/02/2022

"""
beam.py script file to solve equations of a beam in bending to illustrate
the application of the finite difference method.
loading is a function of distance x

x  x  x  x  x  x  x  x  x  x  x  x  x  x  x
___________________________________________
^                                         ^
|                                         |
x=0                                      x=L

Deflection : y

Governing equation: d^2y/dx^2=wLx/(2*E*I)-wx^2/(2*E*I)
Boundary conditions:  y(0)=0 and y(L)=0
Analytical solution: y=(1/(12*E*I))*w*L*(x^3)-(1/(24*E*I))*w*(x^4)-
                    (1/(24*E*I))*w*(L^3)*x
"""

import math
import numpy as np
import matplotlib.pyplot as plt

L = 3               # Beam length (m)
E = 200e9           # Young modulus (Pa)
I = 3e-4            # Moment of inertia (m^4)
w = 15e3            # Uniform load  (N/m)

N = 1001                # Number of nodes
h = L / (N-1)           # Nodal spacing
x = np.array(np.arange(0, L+h, h))     # Nodes

A = np.zeros((N, N))
b = np.zeros((N, 1))

for i in range(N):
    if (i == 0 or i == N-1):
        A[i, i] = 1
        b[i] = 0
    elif (i == 1):
        A[i, i] = -2 / (h**2)
        A[i, i-1] = 0
        A[i, i+1] = 1 / (h**2)
        b[i] = 0.5 * (1 / (E * I)) * w * L * x[i] \
            - 0.5 * (1 / (E * I)) * w * (x[i]**2)
    elif (i == N - 2):
        A[i, i] = -2 / (h**2)
        A[i, i-1] = 1 / (h**2)
        A[i, i+1] = 0
        b[i] = 0.5 * (1 / (E * I)) * w * L * x[i] \
            - 0.5 * (1 / (E * I)) * w * (x[i]**2)
    elif (i > 1 and i < N - 2):
        A[i, i] = -2 / (h**2)
        A[i, i-1] = 1 / (h**2)
        A[i, i+1] = 1 / (h**2)
        b[i] = 0.5 * (1 / (E*I)) * w * L * x[i] \
            - 0.5 * (1 / (E * I)) * w * (x[i]**2)

y = np.linalg.solve(A, b)   # y is the deflection in the beam

# Plot the results
plt.plot([0, L], [0, 0], 'r', label="Undeformed")
plt.plot(x, y, 'b', label="Deformed")
plt.legend()
# plt.show()

# Analytical solution
analytical = (1 / (12 * E * I)) * w * L * (np.power(x, 3)) \
    - (1 / (24 * E * I)) * w * (np.power(x, 4)) \
    - (1 / (24 * E * I)) * w * (L**3) * x

print(np.shape(np.subtract(np.transpose(y), analytical)))
error = \
    math.sqrt(np.mean(np.power(np.subtract(np.transpose(y), analytical), 2))) \
    / abs(np.max(analytical) - np.min(analytical))
print("Normalised root mean square error is %1.6f%%" % (error * 100))
