import numpy as np
from sympy import *
from math import sqrt, radians, degrees # it doesn't work, u may even don't check it
from FK2 import *                       # for some of dots it don't work at all, for others works bad
                                        # i tired of this work

class Dot:
    def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z

def getDistance(dot1, dot2): return sqrt((dot2.x-dot1.x)**2+(dot2.y-dot1.y)**2+(dot2.z-dot1.z)**2)
def htort(h):
    h.col_del(3)
    h.row_del(3)
    transpose(h)
    return h

if __name__ == '__main__':
    q = np.zeros(6)
    sPos = [Dot(0,0,0),Dot(0,0,360),Dot(0,0,780),Dot(0,0,980),Dot(0,0,1180),Dot(0,0,1306),
            Dot(0, 0, 1326)]
    goal = Dot(float(input("X coordinate: ")), float(input("Y coordinate: ")), float(input("Z coordinate: ")))
    while not 420 <= getDistance(sPos[1], goal) <= 966:
        print("goal is unreachable")
        goal = Dot(float(input("X coordinate: ")), float(input("Y coordinate: ")), float(input("Z coordinate: ")))
    q[0] = atan2(goal.x, goal.y)
    flag = False
    if goal.x == 0 and goal.y == 0:
        q[0] = 0
        flag = True # q[0] = [0,2pi]
    r = sqrt(goal.x**2+goal.y**2)
    D = ((goal.z**2+r**2-l2**2-l1**2)/(2*l2*l1))
    print(D)
    q[2] = atan2(sqrt(1000-D**2),D)
    q[1] = atan2(goal.z, sqrt(goal.x**2+goal.y*2)) - atan2(l2*sin(q[2]),l1+l2*sin(q[2]))
    p = htort(Rz(q[0]) * T(l1) * Ry(q[1]) * T(l2) * Ry(q[2]) * T(l3))
    if atan2(p[1,2], p[0,2]) == nan: q[3] = 0.0
    else: q[3] = round(atan2(p[1,2], p[0,2])+q[0],1) % pi
    q[4] = round(atan2(sqrt((p[0, 2])**2+(p[1, 2])**2),p[2,2]),1) % pi
    if q[4] == 0:
        q[4] = 0
        flag = True
    if atan2(p[2,1],p[2,0]) == nan: q[5] = 0
    else: q[5] = round(atan2(p[2,1],p[2,0]),1) % pi
    for i in range(6): print(f"{i}: {(degrees(q[i]))}")
    print(Rz(q[0])*T(l1)*Ry(q[1])*T(l2)*Rx(q[2])*T(l3)*Rz(q[3])*T(l4)*Rx(q[4])*T(l5)*Rz(q[5])*T(l6))
