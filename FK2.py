import numpy as np
from sympy import *
from  math import radians
# constants
l1, l2, l3, l4, l5, l6 = 360, 420, 200, 200, 126, 20
Rlim = 120
RBlim = 170
# for not testing use checking angles
def CheckRot(angle): return angle <= Rlim
def CheckRot2(angle): return angle <= RBlim
#matrix to rotate, translate and FK
def Rx(a): return Matrix([[1, 0, 0, 0], [0, cos(a), -sin(a), 0], [0, sin(a), cos(a), 0], [0, 0, 0, 1]])
def Ry(a): return Matrix([[cos(a), 0, sin(a), 0], [0, 1, 0, 0], [-sin(a), 0, cos(a), 0], [0, 0, 0, 1]])
def Rz(a): return Matrix([[cos(a), -sin(a), 0, 0], [sin(a), cos(a), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
def T(a): return Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, a], [0, 0, 0, 1]])
def FK(q): return Rz(q[0])*T(l1)*Ry(q[1])*T(l2)*Ry(q[2])*T(l3)*Rz(q[3])*T(l4)*Ry(q[4])*T(l5)*Rz(q[5])*T(l6)

if __name__ == '__main__':
    p = FK([0,0,0,0,0,0])
    print("Matrix for standart position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK([0,radians(90),0,0,0,0])
    print("Matrix for max x position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK([0,radians(-90),0,0,0,0])
    print("Matrix for min x position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK([radians(90),radians(90),0,0,0,0])
    print("Matrix for max y position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK([radians(90),radians(-90),0,0,0,0])
    print("Matrix for min y position x =", round(p[0,3],1), " y = ", round(p[1,3],1), "z = ", round(p[2,3],1))
    p = FK([radians(12),radians(45),radians(111),radians(42),radians(11),radians(1)])
    print("Matrix for random position x =", round(p[0,3],5), " y = ", round(p[1,3],5), "z = ", round(p[2,3],5))