# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 20/07/2022
#
# find_root() uses a secant method generalized to 2D to find
# a root of the two equations f1(x,y)=0 and f2(x,y)=0,
# starting from the initial guess x.  Also needed is
# a small interval dx used for estimating the derivatives.
# Both x and dx are 2-element vectors.  The
# names of the function is contained in handle f
# and returns the values of both equations. The function
# must expect a two element input and return a two element output.
# The maximum number of iterations is 40.  The computation
# terminates if ||dx|| < tol.  A root is returned in r.
# The use is
#                r = find_root(func,x0,dx,tol)

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

from derivatives import derivatives

def find_root(func, x, dx, tol):
    if (len(x) != 2 or len(dx) != 2):
        print("x and dx must be two element vectors")
        return

    t0 = 0
    tf = 50

    for i in range(40):
        print("Iteration %i: v = [%.2f %.2f]" % (i+1, x[0], x[1]))
        sol = solve_ivp(derivatives, np.array([t0, tf]), np.array([0, 0, x[0], x[1]]))
        plt.plot(sol.y[0, :], sol.y[1, :], '.r')
        plt.pause(1)

        f0 = np.array(func(x))

        x0 = x + np.array([dx[0], 0])
        print(x0)
        fx = func(x0)
        dfx = (fx - f0) / dx[0]

        x0 = x + np.array([0, dx[1]])
        fy = func(x0)
        dfy = (fy - f0) / dx[1]

        A = np.array([[dfx[0], dfx[1]], [dfy[0], dfy[1]]]) + np.finfo(float).eps
        x = x + dx
        dx = (np.linalg.solve(-A, f0) - np.array(dx))

        if (np.linalg.norm(dx) < tol):
            return x

    print("Still outside tolerance after 40 iterations. abs(dx) = %.3f" % np.abs(dx))
