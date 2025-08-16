# Author: Kim Jiwon
# Date : Started on 2023 / August / 6
# Version: ursina 7.0.0, Python 3.1
# Usage: Run the file with `python3 main.py`


from ursina import *
from cfop_solver import solve

global top
global bottom
global left
global right
global back
global front
top = ["x", "x", "x", "x", "W", "x", "x", "x", "x"] # white
bottom = ["x", "x", "x", "x", "Y", "x", "x", "x", "x"] # yellow
left = ["x", "x", "x", "x", "O", "x", "x", "x", "x"] # orange
right = ["x", "x", "x", "x", "R", "x", "x", "x", "x"] # red
back = ["x", "x", "x", "x", "B", "x", "x", "x", "x"] # blue
front = ["x", "x", "x", "x", "G", "x", "x", "x", "x"] # green

global selectColor
selectColor = "None"

def l0Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        l0.color = color.pink
        l0.highlight_color = color.pink
        left[0] = "R"
    elif selectColor == "B":
        l0.color = color.azure
        l0.highlight_color = color.azure
        left[0] = "B"
    elif selectColor == "G":
        l0.color = color.green
        l0.highlight_color = color.green
        left[0] = "G"
    elif selectColor == "W":
        l0.color = color.white
        l0.highlight_color = color.white
        left[0] = "W"
    elif selectColor == "O":
        l0.color = color.orange
        l0.highlight_color = color.orange
        left[0] = "O"
    elif selectColor == "Y":
        l0.color = color.yellow
        l0.highlight_color = color.yellow
        left[0] = "Y"


def l1Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        l1.color = color.pink
        l1.highlight_color = color.pink
        left[1] = "R"
    elif selectColor == "B":
        l1.color = color.azure
        l1.highlight_color = color.azure
        left[1] = "B"
    elif selectColor == "G":
        l1.color = color.green
        l1.highlight_color = color.green
        left[1] = "G"
    elif selectColor == "W":
        l1.color = color.white
        l1.highlight_color = color.white
        left[1] = "W"
    elif selectColor == "O":
        l1.color = color.orange
        l1.highlight_color = color.orange
        left[1] = "O"
    elif selectColor == "Y":
        l1.color = color.yellow
        l1.highlight_color = color.yellow
        left[1] = "Y"


def l2Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        l2.color = color.pink
        l2.highlight_color = color.pink
        left[2] = "R"
    elif selectColor == "B":
        l2.color = color.azure
        l2.highlight_color = color.azure
        left[2] = "B"
    elif selectColor == "G":
        l2.color = color.green
        l2.highlight_color = color.green
        left[2] = "G"
    elif selectColor == "W":
        l2.color = color.white
        l2.highlight_color = color.white
        left[2] = "W"
    elif selectColor == "O":
        l2.color = color.orange
        l2.highlight_color = color.orange
        left[2] = "O"
    elif selectColor == "Y":
        l2.color = color.yellow
        l2.highlight_color = color.yellow
        left[2] = "Y"


def l3Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        l3.color = color.pink
        l3.highlight_color = color.pink
        left[3] = "R"
    elif selectColor == "B":
        l3.color = color.azure
        l3.highlight_color = color.azure
        left[3] = "B"
    elif selectColor == "G":
        l3.color = color.green
        l3.highlight_color = color.green
        left[3] = "G"
    elif selectColor == "W":
        l3.color = color.white
        l3.highlight_color = color.white
        left[3] = "W"
    elif selectColor == "O":
        l3.color = color.orange
        l3.highlight_color = color.orange
        left[3] = "O"
    elif selectColor == "Y":
        l3.color = color.yellow
        l3.highlight_color = color.yellow
        left[3] = "Y"


def l5Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        l5.color = color.pink
        l5.highlight_color = color.pink
        left[5] = "R"
    elif selectColor == "B":
        l5.color = color.azure
        l5.highlight_color = color.azure
        left[5] = "B"
    elif selectColor == "G":
        l5.color = color.green
        l5.highlight_color = color.green
        left[5] = "G"
    elif selectColor == "W":
        l5.color = color.white
        l5.highlight_color = color.white
        left[5] = "W"
    elif selectColor == "O":
        l5.color = color.orange
        l5.highlight_color = color.orange
        left[5] = "O"
    elif selectColor == "Y":
        l5.color = color.yellow
        l5.highlight_color = color.yellow
        left[5] = "Y"


def l6Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        l6.color = color.pink
        l6.highlight_color = color.pink
        left[6] = "R"
    elif selectColor == "B":
        l6.color = color.azure
        l6.highlight_color = color.azure
        left[6] = "B"
    elif selectColor == "G":
        l6.color = color.green
        l6.highlight_color = color.green
        left[6] = "G"
    elif selectColor == "W":
        l6.color = color.white
        l6.highlight_color = color.white
        left[6] = "W"
    elif selectColor == "O":
        l6.color = color.orange
        l6.highlight_color = color.orange
        left[6] = "O"
    elif selectColor == "Y":
        l6.color = color.yellow
        l6.highlight_color = color.yellow
        left[6] = "Y"


def l7Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        l7.color = color.pink
        l7.highlight_color = color.pink
        left[7] = "R"
    elif selectColor == "B":
        l7.color = color.azure
        l7.highlight_color = color.azure
        left[7] = "B"
    elif selectColor == "G":
        l7.color = color.green
        l7.highlight_color = color.green
        left[7] = "G"
    elif selectColor == "W":
        l7.color = color.white
        l7.highlight_color = color.white
        left[7] = "W"
    elif selectColor == "O":
        l7.color = color.orange
        l7.highlight_color = color.orange
        left[7] = "O"
    elif selectColor == "Y":
        l7.color = color.yellow
        l7.highlight_color = color.yellow
        left[7] = "Y"


def l8Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        l8.color = color.pink
        l8.highlight_color = color.pink
        left[8] = "R"
    elif selectColor == "B":
        l8.color = color.azure
        l8.highlight_color = color.azure
        left[8] = "B"
    elif selectColor == "G":
        l8.color = color.green
        l8.highlight_color = color.green
        left[8] = "G"
    elif selectColor == "W":
        l8.color = color.white
        l8.highlight_color = color.white
        left[8] = "W"
    elif selectColor == "O":
        l8.color = color.orange
        l8.highlight_color = color.orange
        left[8] = "O"
    elif selectColor == "Y":
        l8.color = color.yellow
        l8.highlight_color = color.yellow
        left[8] = "Y"


def f0Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        f0.color = color.pink
        f0.highlight_color = color.pink
        front[0] = "R"
    elif selectColor == "B":
        f0.color = color.azure
        f0.highlight_color = color.azure
        front[0] = "B"
    elif selectColor == "G":
        f0.color = color.green
        f0.highlight_color = color.green
        front[0] = "G"
    elif selectColor == "W":
        f0.color = color.white
        f0.highlight_color = color.white
        front[0] = "W"
    elif selectColor == "O":
        f0.color = color.orange
        f0.highlight_color = color.orange
        front[0] = "O"
    elif selectColor == "Y":
        f0.color = color.yellow
        f0.highlight_color = color.yellow
        front[0] = "Y"


def f1Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        f1.color = color.pink
        f1.highlight_color = color.pink
        front[1] = "R"
    elif selectColor == "B":
        f1.color = color.azure
        f1.highlight_color = color.azure
        front[1] = "B"
    elif selectColor == "G":
        f1.color = color.green
        f1.highlight_color = color.green
        front[1] = "G"
    elif selectColor == "W":
        f1.color = color.white
        f1.highlight_color = color.white
        front[1] = "W"
    elif selectColor == "O":
        f1.color = color.orange
        f1.highlight_color = color.orange
        front[1] = "O"
    elif selectColor == "Y":
        f1.color = color.yellow
        f1.highlight_color = color.yellow
        front[1] = "Y"


def f2Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        f2.color = color.pink
        f2.highlight_color = color.pink
        front[2] = "R"
    elif selectColor == "B":
        f2.color = color.azure
        f2.highlight_color = color.azure
        front[2] = "B"
    elif selectColor == "G":
        f2.color = color.green
        f2.highlight_color = color.green
        front[2] = "G"
    elif selectColor == "W":
        f2.color = color.white
        f2.highlight_color = color.white
        front[2] = "W"
    elif selectColor == "O":
        f2.color = color.orange
        f2.highlight_color = color.orange
        front[2] = "O"
    elif selectColor == "Y":
        f2.color = color.yellow
        f2.highlight_color = color.yellow
        front[2] = "Y"


def f3Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        f3.color = color.pink
        f3.highlight_color = color.pink
        front[3] = "R"
    elif selectColor == "B":
        f3.color = color.azure
        f3.highlight_color = color.azure
        front[3] = "B"
    elif selectColor == "G":
        f3.color = color.green
        f3.highlight_color = color.green
        front[3] = "G"
    elif selectColor == "W":
        f3.color = color.white
        f3.highlight_color = color.white
        front[3] = "W"
    elif selectColor == "O":
        f3.color = color.orange
        f3.highlight_color = color.orange
        front[3] = "O"
    elif selectColor == "Y":
        f3.color = color.yellow
        f3.highlight_color = color.yellow
        front[3] = "Y"


def f5Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        f5.color = color.pink
        f5.highlight_color = color.pink
        front[5] = "R"
    elif selectColor == "B":
        f5.color = color.azure
        f5.highlight_color = color.azure
        front[5] = "B"
    elif selectColor == "G":
        f5.color = color.green
        f5.highlight_color = color.green
        front[5] = "G"
    elif selectColor == "W":
        f5.color = color.white
        f5.highlight_color = color.white
        front[5] = "W"
    elif selectColor == "O":
        f5.color = color.orange
        f5.highlight_color = color.orange
        front[5] = "O"
    elif selectColor == "Y":
        f5.color = color.yellow
        f5.highlight_color = color.yellow
        front[5] = "Y"


def f6Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        f6.color = color.pink
        f6.highlight_color = color.pink
        front[6] = "R"
    elif selectColor == "B":
        f6.color = color.azure
        f6.highlight_color = color.azure
        front[6] = "B"
    elif selectColor == "G":
        f6.color = color.green
        f6.highlight_color = color.green
        front[6] = "G"
    elif selectColor == "W":
        f6.color = color.white
        f6.highlight_color = color.white
        front[6] = "W"
    elif selectColor == "O":
        f6.color = color.orange
        f6.highlight_color = color.orange
        front[6] = "O"
    elif selectColor == "Y":
        f6.color = color.yellow
        f6.highlight_color = color.yellow
        front[6] = "Y"


def f7Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        f7.color = color.pink
        f7.highlight_color = color.pink
        front[7] = "R"
    elif selectColor == "B":
        f7.color = color.azure
        f7.highlight_color = color.azure
        front[7] = "B"
    elif selectColor == "G":
        f7.color = color.green
        f7.highlight_color = color.green
        front[7] = "G"
    elif selectColor == "W":
        f7.color = color.white
        f7.highlight_color = color.white
        front[7] = "W"
    elif selectColor == "O":
        f7.color = color.orange
        f7.highlight_color = color.orange
        front[7] = "O"
    elif selectColor == "Y":
        f7.color = color.yellow
        f7.highlight_color = color.yellow
        front[7] = "Y"


def f8Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        f8.color = color.pink
        f8.highlight_color = color.pink
        front[8] = "R"
    elif selectColor == "B":
        f8.color = color.azure
        f8.highlight_color = color.azure
        front[8] = "B"
    elif selectColor == "G":
        f8.color = color.green
        f8.highlight_color = color.green
        front[8] = "G"
    elif selectColor == "W":
        f8.color = color.white
        f8.highlight_color = color.white
        front[8] = "W"
    elif selectColor == "O":
        f8.color = color.orange
        f8.highlight_color = color.orange
        front[8] = "O"
    elif selectColor == "Y":
        f8.color = color.yellow
        f8.highlight_color = color.yellow
        front[8] = "Y"

def t0Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        t0.color = color.pink
        t0.highlight_color = color.pink
        top[0] = "R"
    elif selectColor == "B":
        t0.color = color.azure
        t0.highlight_color = color.azure
        top[0] = "B"
    elif selectColor == "G":
        t0.color = color.green
        t0.highlight_color = color.green
        top[0] = "G"
    elif selectColor == "W":
        t0.color = color.white
        t0.highlight_color = color.white
        top[0] = "W"
    elif selectColor == "O":
        t0.color = color.orange
        t0.highlight_color = color.orange
        top[0] = "O"
    elif selectColor == "Y":
        t0.color = color.yellow
        t0.highlight_color = color.yellow
        top[0] = "Y"


def t1Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        t1.color = color.pink
        t1.highlight_color = color.pink
        top[1] = "R"
    elif selectColor == "B":
        t1.color = color.azure
        t1.highlight_color = color.azure
        top[1] = "B"
    elif selectColor == "G":
        t1.color = color.green
        t1.highlight_color = color.green
        top[1] = "G"
    elif selectColor == "W":
        t1.color = color.white
        t1.highlight_color = color.white
        top[1] = "W"
    elif selectColor == "O":
        t1.color = color.orange
        t1.highlight_color = color.orange
        top[1] = "O"
    elif selectColor == "Y":
        t1.color = color.yellow
        t1.highlight_color = color.yellow
        top[1] = "Y"


def t2Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        t2.color = color.pink
        t2.highlight_color = color.pink
        top[2] = "R"
    elif selectColor == "B":
        t2.color = color.azure
        t2.highlight_color = color.azure
        top[2] = "B"
    elif selectColor == "G":
        t2.color = color.green
        t2.highlight_color = color.green
        top[2] = "G"
    elif selectColor == "W":
        t2.color = color.white
        t2.highlight_color = color.white
        top[2] = "W"
    elif selectColor == "O":
        t2.color = color.orange
        t2.highlight_color = color.orange
        top[2] = "O"
    elif selectColor == "Y":
        t2.color = color.yellow
        t2.highlight_color = color.yellow
        top[2] = "Y"


def t3Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        t3.color = color.pink
        t3.highlight_color = color.pink
        top[3] = "R"
    elif selectColor == "B":
        t3.color = color.azure
        t3.highlight_color = color.azure
        top[3] = "B"
    elif selectColor == "G":
        t3.color = color.green
        t3.highlight_color = color.green
        top[3] = "G"
    elif selectColor == "W":
        t3.color = color.white
        t3.highlight_color = color.white
        top[3] = "W"
    elif selectColor == "O":
        t3.color = color.orange
        t3.highlight_color = color.orange
        top[3] = "O"
    elif selectColor == "Y":
        t3.color = color.yellow
        t3.highlight_color = color.yellow
        top[3] = "Y"


def t5Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        t5.color = color.pink
        t5.highlight_color = color.pink
        top[5] = "R"
    elif selectColor == "B":
        t5.color = color.azure
        t5.highlight_color = color.azure
        top[5] = "B"
    elif selectColor == "G":
        t5.color = color.green
        t5.highlight_color = color.green
        top[5] = "G"
    elif selectColor == "W":
        t5.color = color.white
        t5.highlight_color = color.white
        top[5] = "W"
    elif selectColor == "O":
        t5.color = color.orange
        t5.highlight_color = color.orange
        top[5] = "O"
    elif selectColor == "Y":
        t5.color = color.yellow
        t5.highlight_color = color.yellow
        top[5] = "Y"


def t6Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        t6.color = color.pink
        t6.highlight_color = color.pink
        top[6] = "R"
    elif selectColor == "B":
        t6.color = color.azure
        t6.highlight_color = color.azure
        top[6] = "B"
    elif selectColor == "G":
        t6.color = color.green
        t6.highlight_color = color.green
        top[6] = "G"
    elif selectColor == "W":
        t6.color = color.white
        t6.highlight_color = color.white
        top[6] = "W"
    elif selectColor == "O":
        t6.color = color.orange
        t6.highlight_color = color.orange
        top[6] = "O"
    elif selectColor == "Y":
        t6.color = color.yellow
        t6.highlight_color = color.yellow
        top[6] = "Y"


def t7Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        t7.color = color.pink
        t7.highlight_color = color.pink
        top[7] = "R"
    elif selectColor == "B":
        t7.color = color.azure
        t7.highlight_color = color.azure
        top[7] = "B"
    elif selectColor == "G":
        t7.color = color.green
        t7.highlight_color = color.green
        top[7] = "G"
    elif selectColor == "W":
        t7.color = color.white
        t7.highlight_color = color.white
        top[7] = "W"
    elif selectColor == "O":
        t7.color = color.orange
        t7.highlight_color = color.orange
        top[7] = "O"
    elif selectColor == "Y":
        t7.color = color.yellow
        t7.highlight_color = color.yellow
        top[7] = "Y"


def t8Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        t8.color = color.pink
        t8.highlight_color = color.pink
        top[8] = "R"
    elif selectColor == "B":
        t8.color = color.azure
        t8.highlight_color = color.azure
        top[8] = "B"
    elif selectColor == "G":
        t8.color = color.green
        t8.highlight_color = color.green
        top[8] = "G"
    elif selectColor == "W":
        t8.color = color.white
        t8.highlight_color = color.white
        top[8] = "W"
    elif selectColor == "O":
        t8.color = color.orange
        t8.highlight_color = color.orange
        top[8] = "O"
    elif selectColor == "Y":
        t8.color = color.yellow
        t8.highlight_color = color.yellow
        top[8] = "Y"


def b0Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        b0.color = color.pink
        b0.highlight_color = color.pink
        bottom[0] = "R"
    elif selectColor == "B":
        b0.color = color.azure
        b0.highlight_color = color.azure
        bottom[0] = "B"
    elif selectColor == "G":
        b0.color = color.green
        b0.highlight_color = color.green
        bottom[0] = "G"
    elif selectColor == "W":
        b0.color = color.white
        b0.highlight_color = color.white
        bottom[0] = "W"
    elif selectColor == "O":
        b0.color = color.orange
        b0.highlight_color = color.orange
        bottom[0] = "O"
    elif selectColor == "Y":
        b0.color = color.yellow
        b0.highlight_color = color.yellow
        bottom[0] = "Y"


def b1Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        b1.color = color.pink
        b1.highlight_color = color.pink
        bottom[1] = "R"
    elif selectColor == "B":
        b1.color = color.azure
        b1.highlight_color = color.azure
        bottom[1] = "B"
    elif selectColor == "G":
        b1.color = color.green
        b1.highlight_color = color.green
        bottom[1] = "G"
    elif selectColor == "W":
        b1.color = color.white
        b1.highlight_color = color.white
        bottom[1] = "W"
    elif selectColor == "O":
        b1.color = color.orange
        b1.highlight_color = color.orange
        bottom[1] = "O"
    elif selectColor == "Y":
        b1.color = color.yellow
        b1.highlight_color = color.yellow
        bottom[1] = "Y"


def b2Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        b2.color = color.pink
        b2.highlight_color = color.pink
        bottom[2] = "R"
    elif selectColor == "B":
        b2.color = color.azure
        b2.highlight_color = color.azure
        bottom[2] = "B"
    elif selectColor == "G":
        b2.color = color.green
        b2.highlight_color = color.green
        bottom[2] = "G"
    elif selectColor == "W":
        b2.color = color.white
        b2.highlight_color = color.white
        bottom[2] = "W"
    elif selectColor == "O":
        b2.color = color.orange
        b2.highlight_color = color.orange
        bottom[2] = "O"
    elif selectColor == "Y":
        b2.color = color.yellow
        b2.highlight_color = color.yellow
        bottom[2] = "Y"


def b3Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        b3.color = color.pink
        b3.highlight_color = color.pink
        bottom[3] = "R"
    elif selectColor == "B":
        b3.color = color.azure
        b3.highlight_color = color.azure
        bottom[3] = "B"
    elif selectColor == "G":
        b3.color = color.green
        b3.highlight_color = color.green
        bottom[3] = "G"
    elif selectColor == "W":
        b3.color = color.white
        b3.highlight_color = color.white
        bottom[3] = "W"
    elif selectColor == "O":
        b3.color = color.orange
        b3.highlight_color = color.orange
        bottom[3] = "O"
    elif selectColor == "Y":
        b3.color = color.yellow
        b3.highlight_color = color.yellow
        bottom[3] = "Y"


def b5Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        b5.color = color.pink
        b5.highlight_color = color.pink
        bottom[5] = "R"
    elif selectColor == "B":
        b5.color = color.azure
        b5.highlight_color = color.azure
        bottom[5] = "B"
    elif selectColor == "G":
        b5.color = color.green
        b5.highlight_color = color.green
        bottom[5] = "G"
    elif selectColor == "W":
        b5.color = color.white
        b5.highlight_color = color.white
        bottom[5] = "W"
    elif selectColor == "O":
        b5.color = color.orange
        b5.highlight_color = color.orange
        bottom[5] = "O"
    elif selectColor == "Y":
        b5.color = color.yellow
        b5.highlight_color = color.yellow
        bottom[5] = "Y"


def b6Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        b6.color = color.pink
        b6.highlight_color = color.pink
        bottom[6] = "R"
    elif selectColor == "B":
        b6.color = color.azure
        b6.highlight_color = color.azure
        bottom[6] = "B"
    elif selectColor == "G":
        b6.color = color.green
        b6.highlight_color = color.green
        bottom[6] = "G"
    elif selectColor == "W":
        b6.color = color.white
        b6.highlight_color = color.white
        bottom[6] = "W"
    elif selectColor == "O":
        b6.color = color.orange
        b6.highlight_color = color.orange
        bottom[6] = "O"
    elif selectColor == "Y":
        b6.color = color.yellow
        b6.highlight_color = color.yellow
        bottom[6] = "Y"


def b7Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        b7.color = color.pink
        b7.highlight_color = color.pink
        bottom[7] = "R"
    elif selectColor == "B":
        b7.color = color.azure
        b7.highlight_color = color.azure
        bottom[7] = "B"
    elif selectColor == "G":
        b7.color = color.green
        b7.highlight_color = color.green
        bottom[7] = "G"
    elif selectColor == "W":
        b7.color = color.white
        b7.highlight_color = color.white
        bottom[7] = "W"
    elif selectColor == "O":
        b7.color = color.orange
        b7.highlight_color = color.orange
        bottom[7] = "O"
    elif selectColor == "Y":
        b7.color = color.yellow
        b7.highlight_color = color.yellow
        bottom[7] = "Y"


def b8Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        b8.color = color.pink
        b8.highlight_color = color.pink
        bottom[8] = "R"
    elif selectColor == "B":
        b8.color = color.azure
        b8.highlight_color = color.azure
        bottom[8] = "B"
    elif selectColor == "G":
        b8.color = color.green
        b8.highlight_color = color.green
        bottom[8] = "G"
    elif selectColor == "W":
        b8.color = color.white
        b8.highlight_color = color.white
        bottom[8] = "W"
    elif selectColor == "O":
        b8.color = color.orange
        b8.highlight_color = color.orange
        bottom[8] = "O"
    elif selectColor == "Y":
        b8.color = color.yellow
        b8.highlight_color = color.yellow
        bottom[8] = "Y"

def r0Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        r0.color = color.pink
        r0.highlight_color = color.pink
        right[0] = "R"
    elif selectColor == "B":
        r0.color = color.azure
        r0.highlight_color = color.azure
        right[0] = "B"
    elif selectColor == "G":
        r0.color = color.green
        r0.highlight_color = color.green
        right[0] = "G"
    elif selectColor == "W":
        r0.color = color.white
        r0.highlight_color = color.white
        right[0] = "W"
    elif selectColor == "O":
        r0.color = color.orange
        r0.highlight_color = color.orange
        right[0] = "O"
    elif selectColor == "Y":
        r0.color = color.yellow
        r0.highlight_color = color.yellow
        right[0] = "Y"


def r1Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        r1.color = color.pink
        r1.highlight_color = color.pink
        right[1] = "R"
    elif selectColor == "B":
        r1.color = color.azure
        r1.highlight_color = color.azure
        right[1] = "B"
    elif selectColor == "G":
        r1.color = color.green
        r1.highlight_color = color.green
        right[1] = "G"
    elif selectColor == "W":
        r1.color = color.white
        r1.highlight_color = color.white
        right[1] = "W"
    elif selectColor == "O":
        r1.color = color.orange
        r1.highlight_color = color.orange
        right[1] = "O"
    elif selectColor == "Y":
        r1.color = color.yellow
        r1.highlight_color = color.yellow
        right[1] = "Y"


def r2Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        r2.color = color.pink
        r2.highlight_color = color.pink
        right[2] = "R"
    elif selectColor == "B":
        r2.color = color.azure
        r2.highlight_color = color.azure
        right[2] = "B"
    elif selectColor == "G":
        r2.color = color.green
        r2.highlight_color = color.green
        right[2] = "G"
    elif selectColor == "W":
        r2.color = color.white
        r2.highlight_color = color.white
        right[2] = "W"
    elif selectColor == "O":
        r2.color = color.orange
        r2.highlight_color = color.orange
        right[2] = "O"
    elif selectColor == "Y":
        r2.color = color.yellow
        r2.highlight_color = color.yellow
        right[2] = "Y"


def r3Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        r3.color = color.pink
        r3.highlight_color = color.pink
        right[3] = "R"
    elif selectColor == "B":
        r3.color = color.azure
        r3.highlight_color = color.azure
        right[3] = "B"
    elif selectColor == "G":
        r3.color = color.green
        r3.highlight_color = color.green
        right[3] = "G"
    elif selectColor == "W":
        r3.color = color.white
        r3.highlight_color = color.white
        right[3] = "W"
    elif selectColor == "O":
        r3.color = color.orange
        r3.highlight_color = color.orange
        right[3] = "O"
    elif selectColor == "Y":
        r3.color = color.yellow
        r3.highlight_color = color.yellow
        right[3] = "Y"


def r5Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        r5.color = color.pink
        r5.highlight_color = color.pink
        right[5] = "R"
    elif selectColor == "B":
        r5.color = color.azure
        r5.highlight_color = color.azure
        right[5] = "B"
    elif selectColor == "G":
        r5.color = color.green
        r5.highlight_color = color.green
        right[5] = "G"
    elif selectColor == "W":
        r5.color = color.white
        r5.highlight_color = color.white
        right[5] = "W"
    elif selectColor == "O":
        r5.color = color.orange
        r5.highlight_color = color.orange
        right[5] = "O"
    elif selectColor == "Y":
        r5.color = color.yellow
        r5.highlight_color = color.yellow
        right[5] = "Y"


def r6Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        r6.color = color.pink
        r6.highlight_color = color.pink
        right[6] = "R"
    elif selectColor == "B":
        r6.color = color.azure
        r6.highlight_color = color.azure
        right[6] = "B"
    elif selectColor == "G":
        r6.color = color.green
        r6.highlight_color = color.green
        right[6] = "G"
    elif selectColor == "W":
        r6.color = color.white
        r6.highlight_color = color.white
        right[6] = "W"
    elif selectColor == "O":
        r6.color = color.orange
        r6.highlight_color = color.orange
        right[6] = "O"
    elif selectColor == "Y":
        r6.color = color.yellow
        r6.highlight_color = color.yellow
        right[6] = "Y"


def r7Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        r7.color = color.pink
        r7.highlight_color = color.pink
        right[7] = "R"
    elif selectColor == "B":
        r7.color = color.azure
        r7.highlight_color = color.azure
        right[7] = "B"
    elif selectColor == "G":
        r7.color = color.green
        r7.highlight_color = color.green
        right[7] = "G"
    elif selectColor == "W":
        r7.color = color.white
        r7.highlight_color = color.white
        right[7] = "W"
    elif selectColor == "O":
        r7.color = color.orange
        r7.highlight_color = color.orange
        right[7] = "O"
    elif selectColor == "Y":
        r7.color = color.yellow
        r7.highlight_color = color.yellow
        right[7] = "Y"


def r8Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        r8.color = color.pink
        r8.highlight_color = color.pink
        right[8] = "R"
    elif selectColor == "B":
        r8.color = color.azure
        r8.highlight_color = color.azure
        right[8] = "B"
    elif selectColor == "G":
        r8.color = color.green
        r8.highlight_color = color.green
        right[8] = "G"
    elif selectColor == "W":
        r8.color = color.white
        r8.highlight_color = color.white
        right[8] = "W"
    elif selectColor == "O":
        r8.color = color.orange
        r8.highlight_color = color.orange
        right[8] = "O"
    elif selectColor == "Y":
        r8.color = color.yellow
        r8.highlight_color = color.yellow
        right[8] = "Y"

def k0Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        k0.color = color.pink
        k0.highlight_color = color.pink
        back[0] = "R"
    elif selectColor == "B":
        k0.color = color.azure
        k0.highlight_color = color.azure
        back[0] = "B"
    elif selectColor == "G":
        k0.color = color.green
        k0.highlight_color = color.green
        back[0] = "G"
    elif selectColor == "W":
        k0.color = color.white
        k0.highlight_color = color.white
        back[0] = "W"
    elif selectColor == "O":
        k0.color = color.orange
        k0.highlight_color = color.orange
        back[0] = "O"
    elif selectColor == "Y":
        k0.color = color.yellow
        k0.highlight_color = color.yellow
        back[0] = "Y"


def k1Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        k1.color = color.pink
        k1.highlight_color = color.pink
        back[1] = "R"
    elif selectColor == "B":
        k1.color = color.azure
        k1.highlight_color = color.azure
        back[1] = "B"
    elif selectColor == "G":
        k1.color = color.green
        k1.highlight_color = color.green
        back[1] = "G"
    elif selectColor == "W":
        k1.color = color.white
        k1.highlight_color = color.white
        back[1] = "W"
    elif selectColor == "O":
        k1.color = color.orange
        k1.highlight_color = color.orange
        back[1] = "O"
    elif selectColor == "Y":
        k1.color = color.yellow
        k1.highlight_color = color.yellow
        back[1] = "Y"


def k2Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        k2.color = color.pink
        k2.highlight_color = color.pink
        back[2] = "R"
    elif selectColor == "B":
        k2.color = color.azure
        k2.highlight_color = color.azure
        back[2] = "B"
    elif selectColor == "G":
        k2.color = color.green
        k2.highlight_color = color.green
        back[2] = "G"
    elif selectColor == "W":
        k2.color = color.white
        k2.highlight_color = color.white
        back[2] = "W"
    elif selectColor == "O":
        k2.color = color.orange
        k2.highlight_color = color.orange
        back[2] = "O"
    elif selectColor == "Y":
        k2.color = color.yellow
        k2.highlight_color = color.yellow
        back[2] = "Y"


def k3Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        k3.color = color.pink
        k3.highlight_color = color.pink
        back[3] = "R"
    elif selectColor == "B":
        k3.color = color.azure
        k3.highlight_color = color.azure
        back[3] = "B"
    elif selectColor == "G":
        k3.color = color.green
        k3.highlight_color = color.green
        back[3] = "G"
    elif selectColor == "W":
        k3.color = color.white
        k3.highlight_color = color.white
        back[3] = "W"
    elif selectColor == "O":
        k3.color = color.orange
        k3.highlight_color = color.orange
        back[3] = "O"
    elif selectColor == "Y":
        k3.color = color.yellow
        k3.highlight_color = color.yellow
        back[3] = "Y"


def k5Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        k5.color = color.pink
        k5.highlight_color = color.pink
        back[5] = "R"
    elif selectColor == "B":
        k5.color = color.azure
        k5.highlight_color = color.azure
        back[5] = "B"
    elif selectColor == "G":
        k5.color = color.green
        k5.highlight_color = color.green
        back[5] = "G"
    elif selectColor == "W":
        k5.color = color.white
        k5.highlight_color = color.white
        back[5] = "W"
    elif selectColor == "O":
        k5.color = color.orange
        k5.highlight_color = color.orange
        back[5] = "O"
    elif selectColor == "Y":
        k5.color = color.yellow
        k5.highlight_color = color.yellow
        back[5] = "Y"


def k6Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        k6.color = color.pink
        k6.highlight_color = color.pink
        back[6] = "R"
    elif selectColor == "B":
        k6.color = color.azure
        k6.highlight_color = color.azure
        back[6] = "B"
    elif selectColor == "G":
        k6.color = color.green
        k6.highlight_color = color.green
        back[6] = "G"
    elif selectColor == "W":
        k6.color = color.white
        k6.highlight_color = color.white
        back[6] = "W"
    elif selectColor == "O":
        k6.color = color.orange
        k6.highlight_color = color.orange
        back[6] = "O"
    elif selectColor == "Y":
        k6.color = color.yellow
        k6.highlight_color = color.yellow
        back[6] = "Y"


def k7Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        k7.color = color.pink
        k7.highlight_color = color.pink
        back[7] = "R"
    elif selectColor == "B":
        k7.color = color.azure
        k7.highlight_color = color.azure
        back[7] = "B"
    elif selectColor == "G":
        k7.color = color.green
        k7.highlight_color = color.green
        back[7] = "G"
    elif selectColor == "W":
        k7.color = color.white
        k7.highlight_color = color.white
        back[7] = "W"
    elif selectColor == "O":
        k7.color = color.orange
        k7.highlight_color = color.orange
        back[7] = "O"
    elif selectColor == "Y":
        k7.color = color.yellow
        k7.highlight_color = color.yellow
        back[7] = "Y"


def k8Click():
    global selectColor
    global top
    global bottom
    global left
    global right
    global back
    global front
    if selectColor == None:
        pass
    elif selectColor == "R":
        k8.color = color.pink
        k8.highlight_color = color.pink
        back[8] = "R"
    elif selectColor == "B":
        k8.color = color.azure
        k8.highlight_color = color.azure
        back[8] = "B"
    elif selectColor == "G":
        k8.color = color.green
        k8.highlight_color = color.green
        back[8] = "G"
    elif selectColor == "W":
        k8.color = color.white
        k8.highlight_color = color.white
        back[8] = "W"
    elif selectColor == "O":
        k8.color = color.orange
        k8.highlight_color = color.orange
        back[8] = "O"
    elif selectColor == "Y":
        k8.color = color.yellow
        k8.highlight_color = color.yellow
        back[8] = "Y"

###################################################################################


global redN
redN = 2
global blueN
blueN = 2
global greenN
greenN = 2
global orangeN
orangeN = 2
global yellowN
yellowN = 2
global whiteN
whiteN = 2

def redClick():
    global selectColor
    global redN
    global blueN
    global greenN
    global orangeN
    global yellowN
    global whiteN
    redN += 1
    selectColor = "R"
    red.text = "√"
    red.text_color = color.black
    red.text_entity.scale /= .7
    if redN % 2 == 0:
        selectColor = None
        red.text = ""
    if blueN % 2 != 0:
        blue.text = ""
        blueN += 1
    if greenN % 2 != 0:
        green.text = ""
        greenN += 1
    if orangeN % 2 != 0:
        orange.text = ""
        orangeN += 1
    if whiteN % 2 != 0:
        white.text = ""
        whiteN += 1
    if yellowN % 2 != 0:
        yellow.text = ""
        yellowN += 1

def blueClick():
    global selectColor
    global redN
    global blueN
    global greenN
    global orangeN
    global yellowN
    global whiteN
    blueN += 1
    selectColor = "B"
    blue.text = "√"
    blue.text_color = color.black
    blue.text_entity.scale /= .7
    if blueN % 2 == 0:
        selectColor = None
        blue.text = ""
    if redN % 2 != 0:
        red.text = ""
        redN += 1
    if greenN % 2 != 0:
        green.text = ""
        greenN += 1
    if orangeN % 2 != 0:
        orange.text = ""
        orangeN += 1
    if whiteN % 2 != 0:
        white.text = ""
        whiteN += 1
    if yellowN % 2 != 0:
        yellow.text = ""
        yellowN += 1


def greenClick():
    global selectColor
    global redN
    global blueN
    global greenN
    global orangeN
    global yellowN
    global whiteN
    greenN += 1
    selectColor = "G"
    green.text = "√"
    green.text_color = color.black
    green.text_entity.scale /= .7
    if greenN % 2 == 0:
        selectColor = None
        green.text = ""
    if blueN % 2 != 0:
        blue.text = ""
        blueN += 1
    if redN % 2 != 0:
        red.text = ""
        redN += 1
    if orangeN % 2 != 0:
        orange.text = ""
        orangeN += 1
    if whiteN % 2 != 0:
        white.text = ""
        whiteN += 1
    if yellowN % 2 != 0:
        yellow.text = ""
        yellowN += 1


def orangeClick():
    global selectColor
    global redN
    global blueN
    global greenN
    global orangeN
    global yellowN
    global whiteN
    orangeN += 1
    selectColor = "O"
    orange.text = "√"
    orange.text_color = color.black
    orange.text_entity.scale /= .7
    if orangeN % 2 == 0:
        selectColor = None
        orange.text = ""
    if blueN % 2 != 0:
        blue.text = ""
        blueN += 1
    if greenN % 2 != 0:
        green.text = ""
        greenN += 1
    if redN % 2 != 0:
        red.text = ""
        redN += 1
    if whiteN % 2 != 0:
        white.text = ""
        whiteN += 1
    if yellowN % 2 != 0:
        yellow.text = ""
        yellowN += 1


def yellowClick():
    global selectColor
    global redN
    global blueN
    global greenN
    global orangeN
    global yellowN
    global whiteN
    yellowN += 1
    selectColor = "Y"
    yellow.text = "√"
    yellow.text_color = color.black
    yellow.text_entity.scale /= .7
    if yellowN % 2 == 0:
        selectColor = None
        yellow.text = ""
    if blueN % 2 != 0:
        blue.text = ""
        blueN += 1
    if greenN % 2 != 0:
        green.text = ""
        greenN += 1
    if orangeN % 2 != 0:
        orange.text = ""
        orangeN += 1
    if whiteN % 2 != 0:
        white.text = ""
        whiteN += 1
    if redN % 2 != 0:
        red.text = ""
        redN += 1


def whiteClick():
    global selectColor
    global redN
    global blueN
    global greenN
    global orangeN
    global yellowN
    global whiteN
    whiteN += 1
    selectColor = "W"
    white.text = "√"
    white.text_color = color.black
    white.text_entity.scale /= .7
    if whiteN % 2 == 0:
        selectColor = None
        white.text = ""
    if blueN % 2 != 0:
        blue.text = ""
        blueN += 1
    if greenN % 2 != 0:
        green.text = ""
        greenN += 1
    if orangeN % 2 != 0:
        orange.text = ""
        orangeN += 1
    if redN % 2 != 0:
        red.text = ""
        redN += 1
    if yellowN % 2 != 0:
        yellow.text = ""
        yellowN += 1




app = Ursina()

scene.clear()

window.title = 'Cube Solover'    
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

################################## color button ####################################
red = Button(position=(-.0, -.45), color = color.pink, highlight_color=color.pink)
red.scale *= .08
red.on_click = redClick

orange = Button(position=(-.735, -.45), color = color.orange, highlight_color=color.orange)
orange.scale *= .08
orange.on_click = orangeClick

green = Button(position=(-.65, -.45), color = color.green, highlight_color=color.green)
green.scale *= .08
green.on_click = greenClick

blue = Button(position=(-.565, -.45), color = color.azure, highlight_color=color.azure)
blue.scale *= .08
blue.on_click = blueClick

yellow = Button(position=(-.48, -.45), color = color.yellow, highlight_color=color.yellow)
yellow.scale *= .08
yellow.on_click = yellowClick

white = Button(position=(-.395, -.45), color = color.white, highlight_color=color.white)
white.scale *= .08
white.on_click = whiteClick



#################################################################################################

l0 = Button(position=(-.545, .07), color = color.gray, highlight_color=color.gray)
l0.scale *= .08
l0.on_click = l0Click

l1 = Button(position=(-.46, .07), color = color.gray, highlight_color=color.gray)
l1.scale *= .08
l1.on_click = l1Click

l2 = Button(position=(-.375, .07), color = color.gray, highlight_color=color.gray)
l2.scale *= .08
l2.on_click = l2Click

l3 = Button(position=(-.545, -.015), color = color.gray, highlight_color=color.gray)
l3.scale *= .08
l3.on_click = l3Click

l4 = Button(position=(-.46, -.015), color = color.orange, highlight_color=color.orange)
l4.scale *= .08

l5 = Button(position=(-.375, -.015), color = color.gray, highlight_color=color.gray)
l5.scale *= .08
l5.on_click = l5Click

l6 = Button(position=(-.545, -.1), color = color.gray, highlight_color=color.gray)
l6.scale *= .08
l6.on_click = l6Click

l7 = Button(position=(-.46, -.1), color = color.gray, highlight_color=color.gray)
l7.scale *= .08
l7.on_click = l7Click

l8 = Button(position=(-.375, -.1), color = color.gray, highlight_color=color.gray)
l8.scale *= .08
l8.on_click = l8Click

##################################################################################################

f0 = Button(position=(-.260, .07), color = color.gray, highlight_color=color.gray)
f0.scale *= .08
f0.on_click = f0Click

f1 = Button(position=(-.175, .07), color = color.gray, highlight_color=color.gray)
f1.scale *= .08
f1.on_click = f1Click

f2 = Button(position=(-.090, .07), color = color.gray, highlight_color=color.gray)
f2.scale *= .08
f2.on_click = f2Click

f3 = Button(position=(-.260, -.015), color = color.gray, highlight_color=color.gray)
f3.scale *= .08
f3.on_click = f3Click

f4 = Button(position=(-.175, -.015), color = color.green, highlight_color=color.green)
f4.scale *= .08

f5 = Button(position=(-.090, -.015), color = color.gray, highlight_color=color.gray)
f5.scale *= .08
f5.on_click = f5Click

f6 = Button(position=(-.260, -.1), color = color.gray, highlight_color=color.gray)
f6.scale *= .08
f6.on_click = f6Click

f7 = Button(position=(-.175, -.1), color = color.gray, highlight_color=color.gray)
f7.scale *= .08
f7.on_click = f7Click

f8 = Button(position=(-.090, -.1), color = color.gray, highlight_color=color.gray)
f8.scale *= .08
f8.on_click = f8Click

##############################################################3

t0 = Button(position=(-.260, .355), color = color.gray, highlight_color=color.gray)
t0.scale *= .08
t0.on_click = t0Click

t1 = Button(position=(-.175, .355), color = color.gray, highlight_color=color.gray)
t1.scale *= .08
t1.on_click = t1Click

t2 = Button(position=(-.090, .355), color = color.gray, highlight_color=color.gray)
t2.scale *= .08
t2.on_click = t2Click

t3 = Button(position=(-.260, .270), color = color.gray, highlight_color=color.gray)
t3.scale *= .08
t3.on_click = t3Click

t4 = Button(position=(-.175, .270), color = color.white, highlight_color=color.white)
t4.scale *= .08

t5 = Button(position=(-.090, .270), color = color.gray, highlight_color=color.gray)
t5.scale *= .08
t5.on_click = t5Click

t6 = Button(position=(-.260, .185), color = color.gray, highlight_color=color.gray)
t6.scale *= .08
t6.on_click = t6Click

t7 = Button(position=(-.175, .185), color = color.gray, highlight_color=color.gray)
t7.scale *= .08
t7.on_click = t7Click

t8 = Button(position=(-.090, .185), color = color.gray, highlight_color=color.gray)
t8.scale *= .08
t8.on_click = t8Click

###############################################################################

b0 = Button(position=(-.260, -.215), color = color.gray, highlight_color=color.gray)
b0.scale *= .08
b0.on_click = b0Click

b1 = Button(position=(-.175, -.215), color = color.gray, highlight_color=color.gray)
b1.scale *= .08
b1.on_click = b1Click

b2 = Button(position=(-.090, -.215), color = color.gray, highlight_color=color.gray)
b2.scale *= .08
b2.on_click = b2Click

b3 = Button(position=(-.260, -.300), color = color.gray, highlight_color=color.gray)
b3.scale *= .08
b3.on_click = b3Click

b4 = Button(position=(-.175, -.300), color = color.yellow, highlight_color=color.yellow)
b4.scale *= .08

b5 = Button(position=(-.090, -.300), color = color.gray, highlight_color=color.gray)
b5.scale *= .08
b5.on_click = b5Click

b6 = Button(position=(-.260, -.385), color = color.gray, highlight_color=color.gray)
b6.scale *= .08
b6.on_click = b6Click

b7 = Button(position=(-.175, -.385), color = color.gray, highlight_color=color.gray)
b7.scale *= .08
b7.on_click = b7Click

b8 = Button(position=(-.090, -.385), color = color.gray, highlight_color=color.gray)
b8.scale *= .08
b8.on_click = b8Click

#############################################################################################

r0 = Button(position=(.025, .07), color = color.gray, highlight_color=color.gray)
r0.scale *= .08
r0.on_click = r0Click

r1 = Button(position=(.110, .07), color = color.gray, highlight_color=color.gray)
r1.scale *= .08
r1.on_click = r1Click

r2 = Button(position=(.195, .07), color = color.gray, highlight_color=color.gray)
r2.scale *= .08
r2.on_click = r2Click

r3 = Button(position=(.025, -.015), color = color.gray, highlight_color=color.gray)
r3.scale *= .08
r3.on_click = r3Click

r4 = Button(position=(.110, -.015), color = color.pink, highlight_color=color.pink)
r4.scale *= .08

r5 = Button(position=(.195, -.015), color = color.gray, highlight_color=color.gray)
r5.scale *= .08
r5.on_click = r5Click

r6 = Button(position=(.025, -.1), color = color.gray, highlight_color=color.gray)
r6.scale *= .08
r6.on_click = r6Click

r7 = Button(position=(.110, -.1), color = color.gray, highlight_color=color.gray)
r7.scale *= .08
r7.on_click = r7Click

r8 = Button(position=(.195, -.1), color = color.gray, highlight_color=color.gray)
r8.scale *= .08
r8.on_click = r8Click

######################################################################################################3

k0 = Button(position=(.310, .07), color = color.gray, highlight_color=color.gray)
k0.scale *= .08
k0.on_click = k0Click

k1 = Button(position=(.395, .07), color = color.gray, highlight_color=color.gray)
k1.scale *= .08
k1.on_click = k1Click

k2 = Button(position=(.480, .07), color = color.gray, highlight_color=color.gray)
k2.scale *= .08
k2.on_click = k2Click

k3 = Button(position=(.310, -.015), color = color.gray, highlight_color=color.gray)
k3.scale *= .08
k3.on_click = k3Click

k4 = Button(position=(.395, -.015), color = color.azure, highlight_color=color.azure)
k4.scale *= .08

k5 = Button(position=(.480, -.015), color = color.gray, highlight_color=color.gray)
k5.scale *= .08
k5.on_click = k5Click

k6 = Button(position=(.310, -.1), color = color.gray, highlight_color=color.gray)
k6.scale *= .08
k6.on_click = k6Click

k7 = Button(position=(.395, -.1), color = color.gray, highlight_color=color.gray)
k7.scale *= .08
k7.on_click = k7Click

k8 = Button(position=(.480, -.1), color = color.gray, highlight_color=color.gray)
k8.scale *= .08
k8.on_click = k8Click

###############################################################################################

global cubeColor
cubeColor = []
global cubeSolution
cubeSolution = []

solveB = Button(position=(.55, -.4), color = color.green, hilight_color=color.green)
solveB.scale = (.2,.1)
solveB.text = "SOLVE"
solveB.text_color = color.black
solveB.text_entity.scale /= .7
def sol():
    global top
    global bottom
    global back
    global front
    global right
    global left
    global redN
    global blueN
    global greenN
    global orangeN
    global yellowN
    global whiteN
    global fillCheck
    fillCheck = 0

    def check(name):
        global fillCheck
        for x in name:
            if x == "x":
                fillCheck = 1


    check(top)
    check(bottom)
    check(right)
    check(left)
    check(front)
    check(back)

    if fillCheck == 0:
        global cubeSolution
        cubeSolution = solve(top, bottom, left, right, back, front, cubeSolution)    
        scene.clear()
        import cube_display


solveB.on_click = sol



# if __name__ == "__main__":
app.run()

