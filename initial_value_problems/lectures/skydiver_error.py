from skydiver import skydiver
from euler_vector import euler_vector

import numpy as np

y1, steps = euler_vector(0, 20, [0], 10, skydiver)
y2, steps = euler_vector(0, 20, [0], 100, skydiver)
y3, steps = euler_vector(0, 20, [0], 1000, skydiver)
y4, steps = euler_vector(0, 20, [0], 10000, skydiver)

C = 0.27
M = 70
g = 9.81
t = 20
exact = (np.sqrt(g) * np.sqrt(M) * np.tanh((np.sqrt(C) * np.sqrt(g) * t) / np.sqrt(M)))/np.sqrt(C)

errors = np.zeros([3,3])
errors[0, :] = [len(y1), y1[-1][0], abs((y1[-1][0] - exact) / exact)]
errors[1, :] = [len(y2), y2[-1][0], abs((y2[-1][0] - exact) / exact)]
errors[2, :] = [len(y3), y3[-1][0], abs((y3[-1][0] - exact) / exact)]

print("Errors for Euler`s method")
print("Steps  V(20)   error")
print("%i   %.6f    %.8f" % (errors[0, 0], errors[0, 1], errors[0, 2]))
print("%i   %.6f    %.8f" % (errors[1, 0], errors[1, 1], errors[1, 2]))
print("%i   %.6f    %.8f" % (errors[2, 0], errors[2, 1], errors[2, 2]))
