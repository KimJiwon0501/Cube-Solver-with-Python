# Author: Kim Jiwon
# Date : Started on 2025 / March / 19
# Version: ursina 7.0.0, Python 3.1
# Usage: Run the file with `python3 main.py` and 'python3 display.py"

from ursina import *
import json

with open("cube_data.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

top = data["top"]
bottom = data["bottom"]
left = data["left"]
right = data["right"]
back = data["back"]
front = data["front"]
solution = data["solution"]
color_map = {"W": "white", "Y": "yellow", "G": "green", "B": "azure", "O": "orange", "R": "pink"}

top = [color_map[color] for color in top]
bottom = [color_map[color] for color in bottom]
left = [color_map[color] for color in left]
right = [color_map[color] for color in right]
back = [color_map[color] for color in back]
front = [color_map[color] for color in front]

app = Ursina()

class Block:
    def __init__(self, front_col, back_col, top_col, bottom_col, right_col, left_col, x, y, z):
        self.entity = Entity(enabled=True)
        self.colors = {
            "front": getattr(color, front_col),
            "back": getattr(color, back_col),
            "top": getattr(color, top_col),
            "bottom": getattr(color, bottom_col),
            "right": getattr(color, right_col),
            "left": getattr(color, left_col)
        }

        self.create_face(self.entity, self.colors["front"], Vec3(0, 0, -1))  # front
        self.create_face(self.entity, self.colors["back"], Vec3(0, 0, 1))   # back
        self.create_face(self.entity, self.colors["right"], Vec3(1, 0, 0))  # right
        self.create_face(self.entity, self.colors["left"], Vec3(-1, 0, 0))  # left
        self.create_face(self.entity, self.colors["top"], Vec3(0, 1, 0))    # top
        self.create_face(self.entity, self.colors["bottom"], Vec3(0, -1, 0))  # bottom

        # 위치 설정
        self.entity.position = Vec3(x, y, z) - Vec3(1, 1, 1)
        self.virtual_position = self.entity.position

    def create_face(self, parent, color, direction):
        e = Entity(parent=parent, model='plane', origin_y=-0.5, texture='white_cube', color=color)
        e.look_at(direction, "up")

    # @property
    # def position(self):
    #     return self.entity.position

    # @position.setter
    # def position(self, value):
    #     self.entity.position = value


corner1 = Block(front[0], "gray", top[6], "gray", "gray", left[2], 0, 2, 0)
corner2 = Block(front[2], "gray", top[8], "gray", right[0], "gray", 2, 2, 0)
corner3 = Block("gray", back[2], top[0], "gray", "gray", left[0], 0, 2, 2)
corner4 = Block("gray", back[0], top[2], "gray", right[2], "gray", 2, 2, 2)
corner5 = Block(front[6], "gray", "gray", bottom[0], "gray", left[8], 0, 0, 0)
corner6 = Block(front[8], "gray", "gray", bottom[2], right[6], "gray", 2, 0, 0)
corner7 = Block("gray", back[8], "gray", bottom[6], "gray", left[6], 0, 0, 2)
corner8 = Block("gray", back[6], "gray", bottom[8], right[8], "gray", 2, 0, 2)

edge1 = Block(front[1], "gray", top[7], "gray", "gray", "gray", 1, 2, 0)
edge2 = Block("gray", "gray", top[3], "gray", "gray", left[1], 0, 2, 1)
edge3 = Block("gray", back[1], top[1], "gray", "gray", "gray", 1, 2, 2)
edge4 = Block("gray", "gray", top[5], "gray", right[1], "gray", 2, 2, 1)
edge5 = Block(front[3], "gray", "gray", "gray", "gray", left[5], 0, 1, 0)
edge6 = Block("gray", back[5], "gray", "gray", "gray", left[3], 0, 1, 2)
edge7 = Block("gray", back[3], "gray", "gray", right[5], "gray", 2, 1, 2)
edge8 = Block(front[5], "gray", "gray", "gray", right[3], "gray", 2, 1, 0)
edge9 = Block(front[7], "gray", "gray", bottom[1], "gray", "gray", 1, 0, 0)
edge10 = Block("gray", "gray", "gray", bottom[3], "gray", left[7], 0, 0, 1)
edge11 = Block("gray", back[7], "gray", bottom[7], "gray", "gray", 1, 0, 2)
edge12 = Block("gray", "gray", "gray", bottom[5], right[7], "gray", 2, 0, 1)

center1 = Block("gray", "gray", top[4], "gray", "gray", "gray", 1, 2, 1)
center2 = Block(front[4], "gray", "gray", "gray", "gray", "gray", 1, 1, 0)
center3 = Block("gray", "gray", "gray", "gray", "gray", left[4], 0, 1, 1)
center4 = Block("gray", back[4], "gray", "gray", "gray", "gray", 1, 1, 2)
center5 = Block("gray", "gray", "gray", "gray", right[4], "gray", 2, 1, 1)
center6 = Block("gray", "gray", "gray", bottom[4], "gray", "gray", 1, 0, 1)


top_block = Entity()
front_block = Entity(parent=scene, position=(0, 0, 0))
right_block = Entity(parent=scene, position=(0, 0, 0))
left_block = Entity(parent=scene, position=(0, 0, 0))
all_block = Entity(parent=scene, position=(0, 0, 0))
middle_block = Entity(parent=scene, position=(0, 0, 0))

def reset():
    for cube in top_block.children:
        cube.world_parent = scene
    for cube in front_block.children:
        cube.world_parent = scene
    for cube in right_block.children:
        cube.world_parent = scene
    for cube in left_block.children:
        cube.world_parent = scene
    for cube in middle_block.children:
        cube.world_parent = scene
    for cube in all_block.children:
        cube.world_parent = scene
    
    top_block.rotation_y = 0  
    front_block.rotation_z = 0  
    right_block.rotation_x = 0  
    left_block.rotation_x = 0  
    middle_block.rotation_x = 0  
    all_block.rotation_y = 0  
    all_block.rotation_x = 0
    all_block.rotation_z = 0   

def rotation(move, top_block, front_block, right_block, left_block, all_block, middle_block, corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, 
             edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12,
             center1, center2, center3, center4, center5, center6):
    
    if move == "U'":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.y >= 0.9:
                cube.entity.world_parent = top_block
        top_block.animate("rotation_y", -90, duration=1.5)



    elif move == "U":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.y >= 0.9:
                cube.entity.world_parent = top_block

        top_block.animate("rotation_y", 90, duration=1.5)

    
    elif move == "R":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.x >= 0.9:
                cube.entity.world_parent = right_block
        right_block.animate("rotation_x", 90, duration=1.5)

    
    elif move == "R'":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.x >= 0.9:
                cube.entity.world_parent = right_block
        right_block.animate("rotation_x", -90, duration=1.5)


    elif move == "F":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.z >= -1 and cube.entity.position.z <= -0.9:
                cube.entity.world_parent = front_block
        front_block.animate("rotation_z", 90, duration=1.5)

    elif move == "F'":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.z >= -1 and cube.entity.position.z <= -0.9:
                cube.entity.world_parent = front_block
        front_block.animate("rotation_z", -90, duration=1.5)
 

    elif move == "L":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.x >= -1 and cube.entity.position.x <= -0.9:
                cube.entity.world_parent = left_block
        left_block.animate("rotation_x", -90, duration=1.5)

    elif move == "L'":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.x >= -1 and cube.entity.position.x <= -0.9:
                cube.entity.world_parent = left_block
        left_block.animate("rotation_x", 90, duration=1.5)

    elif move == "x":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8,
             edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12,
             center1, center2, center3, center4, center5, center6]:
            cube.entity.world_parent = all_block
        all_block.animate("rotation_x", 90, duration=1.5)
        

    elif move == "y":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8,
             edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12,
             center1, center2, center3, center4, center5, center6]:
            cube.entity.world_parent = all_block
        all_block.animate("rotation_y", 90, duration=1.5)
    

    elif move == "y'":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8,
             edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12,
             center1, center2, center3, center4, center5, center6]:
            cube.entity.world_parent = all_block
        all_block.animate("rotation_y", -90, duration=1.5)
    
    elif move == "M":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.x <= 0.1 and cube.entity.position.x >= -0.1:
                cube.entity.world_parent = middle_block
        middle_block.animate("rotation_x", -90, duration=1.5)

    elif move == "M'":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.x <= 0.1 and cube.entity.position.x >= -0.1:
                cube.entity.world_parent = middle_block
        middle_block.animate("rotation_x", 90, duration=1.5)

    elif move == "r":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.x >= -0.1:
                cube.entity.world_parent = right_block
        right_block.animate("rotation_x", 90, duration=1.5)
    
    elif move == "r'":
        for cube in [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, center1, center2, center3, center4, center5, center6]:  # 다른 블록들도 포함할 수 있습니다
            if cube.entity.position.x >= -0.1:
                cube.entity.world_parent = right_block
        right_block.animate("rotation_x", -90, duration=1.5)

    invoke(reset, delay = 1.6)


t = 0
for move in solution:
    t += 2

    invoke(rotation, move, top_block, front_block, right_block, left_block, all_block, middle_block, corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8,
        edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, 
        center1, center2, center3, center4, center5, center6, delay=t)



# camera.position = (15, 7, 8)
# camera.look_at((0, 0, 0))
EditorCamera()



if __name__ == "__main__":
    app.run()