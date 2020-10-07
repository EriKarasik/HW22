import numpy as np
from sympy import *
from math import sqrt, radians, degrees
from FK2 import *
# it still doesn't work, but at least it better than was so i hope to get D
class Dot:
    def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z

def getDistance(dot1, dot2): return sqrt((dot2.x-dot1.x)**2+(dot2.y-dot1.y)**2+(dot2.z-dot1.z)**2)
def IK(goal):
    q = np.zeros(6)
    q[0] = atan2(goal.y, goal.x)
    flag = False
    if goal.x == 0 and goal.y == 0:
        q[0] = 0
        flag = True # q[0] = [0,2pi]
    s = goal.z-l1
    r = sqrt(goal.x**2+goal.y**2)
    l = l3+l4+l5+l6
    D = (l2**2 + l**2 - s**2 - r**2)/(2*l2*l) # cos(pi - q)
    D2 = -(l**2-l2**2-s**2 - r**2)/(2*l2*sqrt(s**2+r**2))
    q[2] = (atan2(D, sqrt(1-D**2)))+pi/2 # instead of writing pi-q[2] just replace arguments
    q[1] = (atan2(s, r) - atan2(D2, sqrt(1-D2**2)))%pi
    p = transpose(Rz(q[0]) * T(l1) * Ry(q[1]) * T(l2) * Ry(q[2]) * T(l3))
    if atan2(p[1,2], p[0,2]) == nan: q[3] = 0.0
    else: q[3] = atan2(p[1,2], p[0,2])%pi
    if atan2(p[2,1],p[2,0]) == nan: q[5] = 0
    else: q[5] = -atan2(p[2,1],p[2,0])%pi
    if atan2(p[1,2]/sin(q[3]),p[2,2]) == nan: q[4] = 0
    else: q[4] = atan2(p[1,2]/sin(q[3]),p[2,2])
    for i in q: print(degrees(i))
    return q

if __name__ == '__main__':
    p = FK(IK(Dot(0,0,1326)))
    print("Matrix for standart position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK(IK(Dot(966, 0, 360)))
    print("Matrix for max x position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK(IK(Dot(-966, 0, 360)))
    print("Matrix for min x position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK(IK(Dot(0, 966, 360)))
    print("Matrix for max y position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK(IK(Dot(0, -966, 360)))
    print("Matrix for min y position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK(IK(Dot(484, 121, 152)))
    print("Matrix for random position x =", round(p[0,3],5), " y = ", round(p[1,3],5), "z = ", round(p[2,3],5))

