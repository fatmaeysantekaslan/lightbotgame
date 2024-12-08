from vpython import *
from time import *

row = 10
column = 10

terrain = [[{"light": False, "height": 0} for i in range(column)] for i in range(row)]

cubes = [[None for i in range(column)] for i in range(row)]

for i in range(row):
    for j in range(column):
        cubes[i][j] = box(
            pos=vector(j, terrain[i][j]["height"] / 2, i),
            size=vector(1, terrain[i][j]["height"] + 1, 1),  
            color=color.blue,  
            opacity=0.8,)

lightbot = sphere(pos=vector(0, 0.5, 0), radius=0.5, color=color.white)

def updateterrain():
    for i in range(row):
        for j in range(column):
            cubes[i][j].pos.y = terrain[i][j]["height"] / 2
            cubes[i][j].size.y = terrain[i][j]["height"] + 1
            if terrain[i][j]["light"]:
                cubes[i][j].color = color.yellow
            else:
                cubes[i][j].color = color.blue

def updatelightbot(x, y, z):
    lightbot.pos = vector(x, z + 0.5, y)

def lightbotvpython(commands):
    global x, y, z
    x, y, z = 0, 0, 0  
    direction = "N"  
    directions = ["N", "E", "S", "W"]

    for command in commands: 
        newx, newy = x, y
        if command == "<":
            direction = directions[(directions.index(direction) + 1) % 4]
        elif command == ">":
            direction = directions[(directions.index(direction) - 1) % 4]
        elif command == "^":
            
            if direction == "N":
                newy += 1
            elif direction == "S":
                newy -= 1
            elif direction == "E":
                newx += 1
            elif direction == "W":
                newx -= 1

            
        if 0 <= newx <= column and 0 <= newy <= row:
                try:
                    height_diff = terrain[newy][newx]["height"] - terrain[y][x]["height"]    
                    if abs(height_diff) == 0:  
                     x, y = newx, newy
                except:
                    print("not possible")
                    
            
        if command == "@":
            terrain[y][x]["light"] = not terrain[y][x]["light"]
        
        elif command == "J":
            
            if direction == "N":
                newy += 1
            elif direction == "S":
                newy -= 1
            elif direction == "E":
                newx += 1
            elif direction == "W":
                newx -= 1

            if 0 <= newx < column and 0 <= newy < row:
                height_diff = terrain[newy][newx]["height"] - terrain[y][x]["height"]
                if abs(height_diff) <= 1:  
                    x, y = newx, newy
                    z += height_diff
        
        updatelightbot(x, y, terrain[y][x]["height"])
        updateterrain()

def set_height(n):
    for (x_co, y_co, height) in n:
        if 0 <= x_co <= column and 0 <= y_co <= row:
            terrain[y_co][x_co]["height"] = height
    updateterrain()

# height setup
set_height([(2, 3, 2), (4, 5, 3), (6, 7, 1)])

commands = "^^<^@"
lightbotvpython(commands)
while True:
    pass