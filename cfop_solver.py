# Author: Kim Jiwon
# Date : Started on 2023 / August / 6
# Version: ursina 7.0.0, Python 3
# Usage: Run the file with `python3.1 main.py`

from cube_rotation import turn, twist, _B, _D, _E, _F, _L, _M, _R, _r, _U, _x, _y, un_B, un_D, un_E, un_F, un_L, un_M, un_R, un_r, un_U, un_x, un_y
import json
import move_optimizer

top = ["W", "W", "W", "W", "W", "W", "W", "W", "W"] # white
bottom = ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"] # yellow
left = ["O", "O", "O", "O", "O", "O", "O", "O", "O"] # orange
right = ["R", "R", "R", "R", "R", "R", "R", "R", "R"] # red
back = ["B", "B", "B", "B", "B", "B", "B", "B", "B"] # blue
front = ["G", "G", "G", "G", "G", "G", "G", "G", "G"] # green


def printCube(top, bottom, left, right, back, front):
    # top
    print("")
    print("        ", top[0], top[1], top[2])
    print("        ", top[3], top[4], top[5])
    print("        ", top[6], top[7], top[8])
    # left, front, right, back
    print("")
    print("", left[0], left[1], left[2], " ", front[0], front[1], front[2], " ", right[0], right[1], right[2], " ", back[0], back[1], back[2])
    print("", left[3], left[4], left[5], " ", front[3], front[4], front[5], " ", right[3], right[4], right[5], " ", back[3], back[4], back[5])
    print("", left[6], left[7], left[8], " ", front[6], front[7], front[8], " ", right[6], right[7], right[8], " ", back[6], back[7], back[8])
    # bottom
    print("")
    print("        ", bottom[0], bottom[1], bottom[2])
    print("        ", bottom[3], bottom[4], bottom[5])
    print("        ", bottom[6], bottom[7], bottom[8])


solution = []

def solve(top, bottom, left, right, back, front, solution):

    def find_color(color_list, target_color):
            return target_color in color_list
    
    color_data = {
        'top': top,
        'bottom': bottom,
        'left': left,
        'right': right,
        'back': back,
        'front': front
    }

    # cube_data.json 파일에 덮어쓰기를 하여 색 데이터 저장
    with open('cube_data.json', 'w') as json_file:
        json.dump(color_data, json_file, indent=4)
    
    # CFOP

    # Cross
    def Cross(top, bottom, left, right, back, front, solution):
    
        while True:
            isFill_top = []
            for i in range(4):
                if find_color(top[1 + (i * 2)], "W") == True:
                    isFill_top += [1 + (i * 2)]
            if len(isFill_top) == 4:
                break
            else:
                isFill_bottom = []  # bottom
                for i in range(4):
                    if find_color(bottom[1 + (i * 2)], "W") == True:
                        isFill_bottom += [1 + (i * 2)]
                        if 1 + (i * 2) == 1:
                            if top[7] != "W":
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            elif top[1] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            elif top[5] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            else:
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                        elif 1 + (i * 2) == 3:
                            if top[3] != "W":
                                top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            elif top[1] != "W":
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            elif top[7] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            else:
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                        elif 1 + (i * 2) == 7:
                            if top[1] != "W":
                                top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            elif top[3] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            elif top[5] != "W":
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            else:
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                        else:
                            if top[5] != "W":
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            elif top[3] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            elif top[1] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                            else:
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_bottom[0]
                
                isFill_front = []  # front
                for i in range(4):
                    if find_color(front[1 + (i * 2)], "W") == True:
                        isFill_front += [1 + (i * 2)]
                        if 1 + (i * 2) == 1:
                            if top[7] != "W":
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            elif top[5] != "W":
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            elif top[3] != "W":
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            else:
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                        elif 1 + (i * 2) == 3:
                            if top[1] != "W":
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            elif top[3] != "W":
                                top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            elif top[5] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            else:
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                        elif 1 + (i * 2) == 5:
                            if top[1] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            elif top[3] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            elif top [5] != "W":
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            else:
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                        else:
                            if top[1] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            elif top[3] != "W":
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            elif top[5] != "W":
                                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]
                            else:
                                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                del isFill_front[0]

                if (find_color(back[1], "W") == True) or (find_color(back[3], "W") == True) or (find_color(back[5], "W") == True) or (find_color(back[7], "W") == True):
                    isFill_back = []  # back
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    for i in range(4):
                        if find_color(front[1 + (i * 2)], "W") == True:
                            isFill_back += [1 + (i * 2)]
                            if 1 + (i * 2) == 1:
                                if top[7] != "W":
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                elif top[5] != "W":
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                else:
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                            elif 1 + (i * 2) == 3:
                                if top[1] != "W":
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                elif top[5] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                else:
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                            elif 1 + (i * 2) == 5:
                                if top[1] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                elif top [5] != "W":
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                else:
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                            else:
                                if top[1] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                elif top[5] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]
                                else:
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_back[0]

                elif (find_color(left[1], "W") == True) or (find_color(left[3], "W") == True) or (find_color(left[5], "W") == True) or (find_color(left[7], "W") == True):
                    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    isFill_left = []  # left
                    for i in range(4):
                        if find_color(front[1 + (i * 2)], "W") == True:
                            isFill_left += [1 + (i * 2)]
                            if 1 + (i * 2) == 1:
                                if top[7] != "W":
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                elif top[5] != "W":
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                else:
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                            elif 1 + (i * 2) == 3:
                                if top[1] != "W":
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                elif top[5] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                else:
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                            elif 1 + (i * 2) == 5:
                                if top[1] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                elif top [5] != "W":
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                else:
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                            else:
                                if top[1] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                elif top[5] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]
                                else:
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_left[0]

                elif(find_color(right[1], "W") == True) or (find_color(right[3], "W") == True) or (find_color(right[5], "W") == True) or (find_color(right[7], "W") == True):
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    isFill_right = []  # right
                    for i in range(4):
                        if find_color(front[1 + (i * 2)], "W") == True:
                            isFill_right += [1 + (i * 2)]
                            if 1 + (i * 2) == 1:
                                if top[7] != "W":
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                elif top[5] != "W":
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                else:
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                            elif 1 + (i * 2) == 3:
                                if top[1] != "W":
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                elif top[5] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                else:
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                            elif 1 + (i * 2) == 5:
                                if top[1] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                elif top [5] != "W":
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                else:
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                            else:
                                if top[1] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                elif top[3] != "W":
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                elif top[5] != "W":
                                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
                                else:
                                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                                    top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                                    del isFill_right[0]
        
        while True:
            if (front[1] == front[4]) and (back[1] == back[4]) and (right[1] == right[4]) and (left[1] == left[4]):
                print("Cross Finish")
                break
            else:
                if front[1] == front[4]:
                    if right[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    elif left[1] == left[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    elif back[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                    else:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                elif left[1] == left[4]:
                    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    if right[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    elif left[1] == left[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    elif back[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                    else:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                elif right[1] == right[4]:
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if right[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    elif left[1] == left[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    elif back[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                    else:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                else:
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if right[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    elif left[1] == left[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    elif back[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                    else:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)

    def F2L1(top, bottom, left, right, back, front, solution): #F2L2

        top, bottom, left, right, back, front, solution = _x(top, bottom, left, right, back, front, solution)
        top, bottom, left, right, back, front, solution = _x(top, bottom, left, right, back, front, solution)



        while True:
            if (
                    (bottom[0] == bottom[4]) and (bottom[2] == bottom[4]) and (bottom[6] == bottom[4]) and (bottom[8] == bottom[4]) and 
                    (front[6] == front[4]) and (front[8] == front[4]) and (back[6] == back[4]) and (back[8] == back[4]) and 
                    (left[6] == left[4]) and (left[8] == left[4]) and (right[6] == right[4]) and (right[8] == right[4])
            ):
                print("F2L1 Finish")
                break
            elif (top[0] == "W") or (top[2] == "W") or (top[6] == "W") or (top[8] == "W"):
                if top[8] == "W":
                    if front[4] == right[0]:
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                    elif front[4] != right[0]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                elif top[2] == "W":
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if front[4] == right[0]:
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                    elif front[4] != right[0]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                elif top[6] == "W":
                    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    if front[4] == right[0]:
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                    elif front[4] != right[0]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                else:
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if front[4] == right[0]:
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                    elif front[4] != right[0]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
            elif (front[2] == "W") or (right[2] == "W") or (back[2] == "W") or (left[2] == "W"):
                if front[2] == "W":
                    if top[8] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                    elif top[8] != front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                elif right[2] == "W":
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if top[8] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                    elif top[8] != front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                elif left[2] == "W":
                    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    if top[8] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                    elif top[8] != front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                else:
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if top[8] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                    elif top[8] != front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
            elif (front[0] == "W") or (back[0] == "W") or (right[0] == "W") or (left[0] == "W"):
                if front[0] == "W":
                    if top[6] == front[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                    elif top[6] != front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                elif back[0] == "W":
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if top[6] == front[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                    elif top[6] != front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                elif right[0] == "W":
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if top[6] == front[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                    elif top[6] != front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                elif left[0] == "W":
                    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    if top[6] == front[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                    elif top[6] != front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
            elif (front[8] == "W") or (back[8] == "W") or (right[8] == "W") or (left[8] == "W"):
                if front[8] == "W":
                    if right[6] == front[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                    elif right[6] != front[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                elif back[8] == "W":
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if right[6] == front[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                    elif right[6] != front[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                elif right[8] == "W":
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if right[6] == front[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                    elif right[6] != front[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                elif left[8] == "W":
                    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    if right[6] == front[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                    elif right[6] != front[4]:
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
            elif (front[6] == "W") or (back[6] == "W") or (right[6] == "W") or (left[6] == "W"):
                if front[6] == "W":
                    if left[8] == front[4]:
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                    elif left[8] != front[4]:
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                elif right[6] == "W":
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if left[8] == front[4]:
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                    elif left[8] != front[4]:
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                elif left[6] == "W":
                    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    if left[8] == front[4]:
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                    elif left[8] != front[4]:
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                elif back[6] == "W":
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    if left[8] == front[4]:
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                    elif left[8] != front[4]:
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)

    def F2L2(top, bottom, left, right, back, front, solution): #F2L2


        while True:
            if (
                    (front[3] == front[4]) and (front[5] == front[4]) and (left[3] == left[4]) and (left[5] == left[4]) and 
                    (right[3] == right[4]) and (right[5] == right[4]) and (back[3] == back[4]) and (back[5] == back[4])
            ):
                print("F2L2 Finish")
                break
            
            else:
                if (front[1] == front[4]) and (top[7] != "Y"):
                    if top[7] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                    elif top[7] == left[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                
                elif (right[1] == right[4]) and (top[5] != "Y"):
                    if top[5] == back[4]:
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                    elif top[5] == front[4]:
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                elif top[7] == left[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                
                elif (left[1] == left[4]) and (top[3] != "Y"):
                    if top[3] == front[4]:
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                    elif top[3] == back[4]:
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                elif top[7] == left[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                
                elif (back[1] == back[4]) and (top[1] != "Y"):
                    if top[1] == left[4]:
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                    elif top[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _L(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                
                elif (front[5] != front[4]) and (front[5] != "Y") and (right[3] != "Y"):
                    top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                    if back[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    elif back[1] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    elif back[1] == left[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    elif back[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                
                elif (right[5] != right[4]) and (right[5] != "Y") and (back[3] != "Y"):
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                    if back[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    elif back[1] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    elif back[1] == left[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    elif back[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)

                elif (left[5] != left[4]) and (left[5] != "Y") and (front[3] != "Y"):
                    top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                    if back[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    elif back[1] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    elif back[1] == left[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    elif back[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)

                elif (back[5] != back[4]) and (back[5] != "Y") and (left[3] != "Y"):
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                    if back[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    elif back[1] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    elif back[1] == left[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    elif back[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)

                elif (front[1] != "Y") and (top[7] != "Y"):
                    if front[1] == right[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    elif front[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    elif front[1] == left[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                
                elif (right[1] != "Y") and (top[5] != "Y"):
                    if right[1] == back[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    elif right[1] == left[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    elif right[1] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                
                elif (back[1] != "Y") and (top[1] != "Y"):
                    if back[1] == left[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = un_y(top, bottom, left, right, back, front, solution)
                    elif back[1] == front[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    elif back[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                
                elif (left[1] != "Y") and (top[3] != "Y"):
                    if left[1] == front[4]:
                        top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    elif left[1] == right[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                    elif left[1] == back[4]:
                        top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)
                        top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)


    def OLL1(top, bottom, left, right, back, front, solution): # OLL1

        while True:
            if (
                    (top[1] == "Y") and (top[3] == "Y") and (top[5] == "Y") and (top[7] == "Y")
            ):
                print("OLL1 Finish")
                break

            elif (top[1] != "Y") and (top[3] != "Y") and (top[5] != "Y") and (top[7] != "Y"):
                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
            
            elif (top[1] == "Y") and (top[3] == "Y"):
                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
            
            elif (top[3] == "Y") and (top[5] == "Y"):
                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)

            else:
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)

    
    def OLL2(top, bottom, left, right, back, front, solution): # OLL2

        while True:
            if (
                    (top[0] == "Y") and (top[2] == "Y") and (top[6] == "Y") and (top[8] == "Y")
            ):
                print("OLL2 Finish")
                break

            elif (top[6] == "Y") and (back[2] == "Y") and (right[2] == "Y") and (front[2] == "Y"):
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
            
            elif (top[0] == "Y") and (back[0] == "Y") and (right[0] == "Y") and (front[0] == "Y"):
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)

            elif (left[0] == "Y") and (left[2] == "Y") and (right[0] == "Y") and (right[2] == "Y"):
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
            
            elif (top[2] == "Y") and (top[6] == "Y") and (left[0] == "Y") and (front[2] == "Y"):
                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _r(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_r(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
            
            elif (front[0] == "Y") and (back[2] == "Y") and (top[2] == "Y") and (top[8] == "Y"):
                top, bottom, left, right, back, front, solution = _r(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_r(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)

            elif (front[0] == "Y") and (front[2] == "Y") and (top[0] == "Y") and (top[2] == "Y"):
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _D(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_D(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
            
            elif (front[2] == "Y") and (back[0] == "Y") and (left[0] == "Y") and (left[2] == "Y"):
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
        
            else:
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)

    
    def PLL1(top, bottom, left, right, back, front, solution): # PLL1

        while True:
            if (front[0] == front[2]) and (back[0] == back[2]) and (right[0] == right[2]) and (left[0] == left[2]):
                print("PLL1 Finish")
                break

            elif left[0] == left[2]:
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = twist(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
            
            elif back[0] == back[2]:
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
            
            elif front[0] == front[2]:
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
            
            elif right[0] == right[2]:
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)

            else:
                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _F(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _R(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_F(top, bottom, left, right, back, front, solution)

    def PLL2(top, bottom, left, right, back, front, solution): # PLL2

        while True:
            if (front[0] == front[4]) and (right[0] == right[4]) and (back[0] == back[4]) and (left[0] == left[4]):
                print("PLL2 Finish")
                break
            
            else:
                top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)


    def PLL3(top, bottom, left, right, back, front, solution): # PLL3

        while True:
            if (front[1] == front[4]) and (left[1] == left[4]) and (back[1] == back[4]) and (right[1] == right[4]):
                print("PLL3 Finish")
                break
            
            elif front[1] == front[4]:
                if back[1] == left[4]:
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                
                elif back[1] == right[4]:
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                    top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)

            elif (front[1] == back[4]) and (right[1] == left[4]):
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
            
            elif (front[1] == left[4]) and (left[1] == front[4]):
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = _M(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
                top, bottom, left, right, back, front, solution = un_U(top, bottom, left, right, back, front, solution)
            
            else:
                top, bottom, left, right, back, front, solution = _y(top, bottom, left, right, back, front, solution)

    Cross(top, bottom, left, right, back, front, solution)
    F2L1(top, bottom, left, right, back, front, solution)
    F2L2(top, bottom, left, right, back, front, solution)
    OLL1(top, bottom, left, right, back, front, solution)
    OLL2(top, bottom, left, right, back, front, solution)
    PLL1(top, bottom, left, right, back, front, solution)
    PLL2(top, bottom, left, right, back, front, solution)
    PLL3(top, bottom, left, right, back, front, solution)

#TEST
    # if (front[0] == front[1]) and (front[1] == front[2]) and (front[2] == front[3]) and (front[3] == front[4]) and (front[4] == front[5]) and (front[5] == front[6]) and (front[3] == front[7]) and (front[3] == front[8]) and (back[0] == back[1]) and (back[1] == back[2]) and (back[2] == back[3]) and (back[3] == back[4]) and (back[4] == back[5]) and (back[5] == back[6]) and (back[3] == back[7]) and (back[3] == back[8]) and (top[0] == top[1]) and (top[1] == top[2]) and (top[2] == top[3]) and (top[3] == top[4]) and (top[4] == top[5]) and (top[5] == top[6]) and (top[3] == top[7]) and (top[3] == top[8]) and (bottom[0] == bottom[1]) and (bottom[1] == bottom[2]) and (bottom[2] == bottom[3]) and (bottom[3] == bottom[4]) and (bottom[4] == bottom[5]) and (bottom[5] == bottom[6]) and (bottom[3] == bottom[7]) and (bottom[3] == bottom[8]) and (left[0] == left[1]) and (left[1] == left[2]) and (left[2] == left[3]) and (left[3] == left[4]) and (left[4] == left[5]) and (left[5] == left[6]) and (left[3] == left[7]) and (left[3] == left[8]) and (right[0] == right[1]) and (right[1] == right[2]) and (right[2] == right[3]) and (right[3] == right[4]) and (right[4] == right[5]) and (right[5] == right[6]) and (right[3] == right[7]) and (right[3] == right[8]):
    #     print("TRUE")
        
    solution = move_optimizer.process_with_shortening(solution)
    print(solution)

# 기존 데이터를 읽어오기
    try:
        with open('cube_data.json', 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}

    # 기존 데이터에 솔루션 추가
    existing_data['solution'] = solution

    # data.json 파일에 솔루션 추가 (덮어쓰기)
    with open('cube_data.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    return solution