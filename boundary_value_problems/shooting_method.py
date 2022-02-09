# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 09/02/2022

from eulers import eulers # import the eulers function from the eulers file
import numpy as np
import matplotlib.pyplot as plt

# Let's define our system of differential equations
def dudr(r, u, w): return w
def dwdr(r, u, w): return -w/r + u/r**2

# now we need to define some boundary conditions
r_a = 5              # Inner radius
r_b = 8              # Outer radius
et_a = 7.7462e-4     # Tangential strains
et_b = 3.8462e-4
u_a = r_a * et_a     # Radial dsplacements
u_b = r_b * et_b

# We need an informed guess to use as a starting point for w
# The way to get this is to think about how we've defined w
# ie w represents the change in displacement with respect to a change in radius
# The BC values at either end point can be used to make an informed guess at w
w_a = (u_b - u_a) / (r_b - r_a)

# Now we set up some looping parameters
distance = r_b - r_a
steps = 4
h = distance / steps

# We now have enough information to try using Euler's method with a naive guess
solution = eulers(dudr, dwdr, np.arange(r_a, r_b+h, h), u_a, w_a)

# Cool we've got our first set of data we should plot it!
plt.plot(solution[:, 0], solution[:, 1], label="Initial guess")
plt.scatter([r_a, r_b], [u_a, u_b], label="Boundary values")
plt.grid()
# plt.show()

# OK, so our first guess wasn't fantastic, we didn't hit the target boundary value
# We should try and take another guess at w_a. We could try anything but
# Let's try just see what doubling it does
sol = eulers(dudr, dwdr, np.arange(r_a, r_b+h, h), u_a, 2*w_a)

# We're getting a bit of data now so let's stack the 2 2D arrays on top of each other
# and make them into one 3D array
solution = np.stack((solution, sol), 2)

# Now, let's plot our newest guess
plt.clf()
plt.plot(solution[:, 0, 0], solution[:, 1, 0], label="Initial guess")
plt.plot(solution[:, 0, 1], solution[:, 1, 1], label="Second guess")
plt.scatter([r_a, r_b], [u_a, u_b], label="Boundary values")
plt.grid()
plt.legend()
# plt.show()

# Hmm, this still isn't very good. The question to ask is, what's the best way to
# use the information we've just learned to inform our next guess.
# The answer is to use a root finding algorithm to look for the initial guess
# That results in the least error between the proposed u_b and the true value.
def error(u_guess): return u_b - u_guess

# Linear interpolation will give us the right initial conditions because
# this is a linear ODE. If the ODE was non-linear we would have to use an
# iterative root-finding method like the secant method to find the best w_a.
def lin_interp(u_old, u_new, w_old, w_new):
    return w_new - error(u_new) * (w_new - w_old) / (error(u_new) - error(u_old))

ub_old = solution[-1, 1, 0]
ub_new = solution[-1, 1, 1]
wa_old = solution[0, 2, 0]
wa_new = solution[0, 2, 1]

wa_final = lin_interp(ub_old, ub_new, wa_old, wa_new)

sol = eulers(dudr, dwdr, np.arange(r_a, r_b+h, h), u_a, wa_final)
solution = np.stack((solution[:, :, 0], solution[:, :, 1], sol), 2)

# We've got some more data so let's plot itand check we've got it right
plt.clf()
plt.plot(solution[:, 0, 0], solution[:, 1, 0], label="Initial guess")
plt.plot(solution[:, 0, 1], solution[:, 1, 1], label="Second guess")
plt.plot(solution[:, 0, 2], solution[:, 1, 2], label="Final guess")
plt.scatter([r_a, r_b], [u_a, u_b], label="Boundary values")
plt.grid()
plt.legend()
plt.show()
