# Author: Kim Jiwon
# Date : Started on 2023 / August / 6
# Version: ursina 7.0.0, Python 3.1
# Usage: Run the file with `python3 main.py`

def turn(self):
    x = [0, 1, 2]
    x[2] = self[2]
    self[2] = self[0]
    self[0] = self[6]
    self[6] = self[8]
    self[8] = x[2]
    x[1] = self[1]
    self[1] = self[3]
    self[3] = self[7]
    self[7] = self[5]
    self[5] = x[1]
    return self

def _U(top, bottom, left, right, back, front, solution):
    x = [0, 1, 2]
    for i in range(3):
        x[i] = left[i]
        left[i] = front[i]
        front[i] = right[i]
        right[i] = back[i]
        back[i] = x[i]
    top = turn(top)
    solution.append("U")
    return top, bottom, left, right, back, front, solution

def un_U(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _U(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _U(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _U(top, bottom, left, right, back, front, x)
    solution.append("U'")
    return top, bottom, left, right, back, front, solution

def _F(top, bottom, left, right, back, front, solution):
    x = [0, 1, 2]
    x[0] = right[0]
    x[1] = right[3]
    x[2] = right[6]
    right[0] = top[6]
    right[3] = top[7]
    right[6] = top[8]
    top[6] = left[8]
    top[7] = left[5]
    top[8] = left[2]
    left[8] = bottom[2]
    left[5] = bottom[1]
    left[2] = bottom[0]
    bottom[2] = x[0]
    bottom[1] = x[1]
    bottom[0] = x[2]
    front = turn(front)
    solution.append("F")
    return top, bottom, left, right, back, front, solution


def un_F(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _F(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _F(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _F(top, bottom, left, right, back, front, x)
    solution.append("F'")
    return top, bottom, left, right, back, front, solution

def _R(top, bottom, left, right, back, front, solution):
    x = [0, 1, 2]
    for i in range(3):
        x[i] = top[i + 2 + (i * 2)]
        top[i + 2 + (i * 2)] = front[i + 2 + (i * 2)]
        front[i + 2 + (i * 2)] = bottom[i + 2 + (i * 2)]
    bottom[2] = back[6]
    bottom[5] = back[3]
    bottom[8] = back[0]
    back[0] = x[2]
    back[3] = x[1]
    back[6] = x[0]
    right = turn(right)
    solution.append("R")
    return top, bottom, left, right, back, front, solution

def un_R(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _R(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _R(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _R(top, bottom, left, right, back, front, x)
    solution.append("R'")
    return top, bottom, left, right, back, front, solution

def _L(top, bottom, left, right, back, front, solution):
    x = [0, 1, 2]
    x[0] = front[0]
    x[1] = front[3]
    x[2] = front[6]
    front[0] = top[0]
    front[3] = top[3]
    front[6] = top[6]
    top[0] = back[8]
    top[3] = back[5]
    top[6] = back[2]
    back[8] = bottom[0]
    back[5] = bottom[3]
    back[2] = bottom[6]
    bottom[0] = x[0]
    bottom[3] = x[1]
    bottom[6] = x[2]
    left = turn(left)
    solution.append("L")
    return top, bottom, left, right, back, front, solution

def un_L(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _L(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _L(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _L(top, bottom, left, right, back, front, x)
    solution.append("L'")
    return top, bottom, left, right, back, front, solution


def _M(top, bottom, left, right, back, front, solution):
    x = [0, 1, 2]
    x[0] = front[1]
    x[1] = front[4]
    x[2] = front[7]
    front[1] = top [1]
    front[4] = top[4]
    front[7] = top[7]
    top[1] = back[7]
    top[4] = back[4]
    top[7] = back[1]
    back[7] = bottom[1]
    back[4] = bottom[4]
    back[1] = bottom[7]
    bottom[1] = x[0]
    bottom[4] = x[1]
    bottom[7] = x[2]
    solution.append("M")
    return top, bottom, left, right, back, front, solution

def un_M(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _M(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _M(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _M(top, bottom, left, right, back, front, x)
    solution.append("M'")
    return top, bottom, left, right, back, front, solution

def _x(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _R(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_L(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_M(top, bottom, left, right, back, front, x)
    solution.append("x")
    return top, bottom, left, right, back, front, solution

def un_x(top, bottom, left, right, back, front, solution):
    top, bottom, left, right, back, front, solution = _x(top, bottom, left, right, back, front, solution)
    top, bottom, left, right, back, front, solution = _x(top, bottom, left, right, back, front, solution)
    top, bottom, left, right, back, front, solution = _x(top, bottom, left, right, back, front, solution)
    return top, bottom, left, right, back, front, solution

def _D(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _x(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _F(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_x(top, bottom, left, right, back, front, x)
    solution.append("D")
    return top, bottom, left, right, back, front, solution

def un_D(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _x(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_F(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_x(top, bottom, left, right, back, front, x)
    solution.append("D'")
    return top, bottom, left, right, back, front, solution

def _r(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _R(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_M(top, bottom, left, right, back, front, x)
    solution.append("r")
    return top, bottom, left, right, back, front, solution

def un_r(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = un_R(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _M(top, bottom, left, right, back, front, x)
    solution.append("r'")
    return top, bottom, left, right, back, front, solution

def _E(top, bottom, left, right, back, front, solution):
    x = [0, 1, 2]
    for i in range(3):
        x[i] = front[i + 3]
        front[i + 3] = left[i + 3]
        left[i + 3] = back[i + 3]
        back[i + 3] = right[i + 3]
        right[i + 3] = x[i]
    return top, bottom, left, right, back, front, solution

def un_E(top, bottom, left, right, back, front, solution):
    top, bottom, left, right, back, front, solution = _E(top, bottom, left, right, back, front, solution)
    top, bottom, left, right, back, front, solution = _E(top, bottom, left, right, back, front, solution)
    top, bottom, left, right, back, front, solution = _E(top, bottom, left, right, back, front, solution)
    return top, bottom, left, right, back, front, solution

def _y(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _U(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_E(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_D(top, bottom, left, right, back, front, x)
    solution.append("y")
    return top, bottom, left, right, back, front, solution

def un_y(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _y(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _y(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _y(top, bottom, left, right, back, front, x)
    solution.append("y'")
    return top, bottom, left, right, back, front, solution

def _B(top, bottom, left, right, back, front, solution):
    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
    return top, bottom, left, right, back, front, solution

def un_B(top, bottom, left, right, back, front, solution):
    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
    top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
    return top, bottom, left, right, back, front, solution

def twist(top, bottom, left, right, back, front, solution):
    x = []
    top, bottom, left, right, back, front, x = _R(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = _U(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_R(top, bottom, left, right, back, front, x)
    top, bottom, left, right, back, front, x = un_U(top, bottom, left, right, back, front, x)
    solution.append("R")
    solution.append("U")
    solution.append("R'")
    solution.append("U'")
    return top, bottom, left, right, back, front, solution