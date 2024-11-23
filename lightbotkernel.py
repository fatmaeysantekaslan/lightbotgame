x, y, z = 0, 0, 0
direction = "N"
row = 10
column = 10

terrain = [[{"light":False, "height":0} for i in range(column)] for i in range(row)]

def left():
  global direction
  directions = ["N", "W", "S", "E"]
  direction = directions[(directions.index(direction) + 1) % 4]

def right():
  global direction
  directions = ["N", "E", "S", "W"]
  direction = directions[(directions.index(direction) + 1) % 4]

def move():
  global x, y
  newx, newy = x, y
  if direction == "N" and y < row - 1:
    newy += 1
  elif direction == "S" and y > 0:
    newy += -1
  elif direction == "E" and x < column - 1:
    newx += 1
  elif direction == "W" and x > 0:
    newx += -1
  x, y = newx, newy

def jump():
  global x, y, z
  newx, newy = x, y
  if direction == "N" and y < row - 1:
    newy += 1
  elif direction == "S" and y > 0:
    newy += -1
  elif direction == "E" and x < column - 1:
    newx += 1
  elif direction == "W" and x > 0:
    newx += -1

  difference = terrain[newy][newx]["height"] - terrain[y][x]["height"]
  if abs(difference) == 1:
    x, y = newx, newy
    z += difference

def set_height(n):
  for (x_co, y_co, height) in n:
    if 0 <= x_co < column and 0 <= y_co < row:
      terrain[y_co][x_co]["height"] = height

def light():
  global terrain
  if terrain[y][x]["light"]:
    terrain[y][x]["light"] = False
  else:
    terrain[y][x]["light"] = True

def lightbot(commands):
  for command in commands:
    if command == "<":
      left()
    elif command == ">":
      right()
    elif command == "^":
      move()
    elif command == "@":
      light()

    print("Position:", (x, y, z), "Direction:", direction)
    print("Light status at", (x, y, z), ":", 'ON' if terrain[y][x]["light"] else 'OFF')


#commands = "^^>^<^@"
#lightbot(commands)