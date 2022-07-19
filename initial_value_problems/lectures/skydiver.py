# Author: Gerry Gralton
# E-mail: gerry.gralton@uwa.edu.au
# Date: 19/07/2022
#
# f_skydiver(x,y) gives the right side of equation v'(t)=-C/M v^2 +g
# M is a mass of the skydiver, C is the aerodynamical drag coefficient,
# g is the gravity acceleration

def skydiver(t, v):
    C = 0.27
    M = 70
    g = 9.81

    return -C/ M * v**2 + g
