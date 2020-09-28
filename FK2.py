import numpy as np
from sympy import *
import math

l1, l2, l3, l4, l5, l6 = 360, 420, 200, 200, 126, 20
Rlim = 120
RBlim = 170

def CheckRot(angle): return angle <= Rlim
def CheckRot2(angle): return angle <= RBlim

def Rx(a): return Matrix([[1, 0, 0, 0], [0, cos(a), -sin(a), 0], [0, sin(a), cos(a), 0], [0, 0, 0, 1]])
def Ry(a): return Matrix([[cos(a), 0, sin(a), 0], [0, 1, 0, 0], [-sin(a), 0, cos(a), 0], [0, 0, 0, 1]])
def Rz(a): return Matrix([[cos(a), -sin(a), 0, 0], [sin(a), cos(a), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
def T(a): return Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, a], [0, 0, 0, 1]])

if __name__ == '__main__':
    q = np.zeros(6)
    for i in range(6):
        q[i] = math.radians(float(input(f"q{i+1} degrees: ")) % 180)
        if i == 0 or i == 3:
            while not CheckRot(q[i]):
                print(f"q{i+1} should be in range(-120, 120) degrees")
                q[i] = math.radians(float(input(f"q{i+1} degrees: ")) % 180)
        elif i != 6:
            while not CheckRot2(q[i]):
                print(f"q{i+1} should be in range(-170, 170) degrees")
                q[i] = math.radians(float(input(f"q{i+1} degrees: ")) % 180)
    p = Rz(q[0])*T(l1)*Ry(q[1])*T(l2)*Ry(q[2])*T(l3)*Ry(q[3])*T(l4)*Ry(q[4])*T(l5)*Ry(q[5])*T(l6)
    print(p)