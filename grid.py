import random

# 0 = Center
# -1 = Left
# 1 = Right
# 1 = Up
# -1 = Down

names = {
    "0": "□",
    "1": "■",
}

class Map:
    def __init__(self, width = 100, height = 100):
        self.grid = []
        self.width = width
        self.height = height

    def setup(self):
        for x in range(self.width):
            self.grid.append([Object(random.randint(0,1)) for y in range(self.height)])
        return self

    def update(self):
        for x in range(self.width):
            for y in range(self.height):
                obj = self.grid[y][x]
                if obj.type == 1 and not obj.nearby == 2 and not obj.nearby == 3:
                    obj.type = 0
                elif obj.type == 0 and obj.nearby == 3:
                    obj.type = 1
                obj.nearby = 0

    def display(self):

        print("\n".join([" ".join([names[str(x.type)] for x in y]) for y in self.grid]))

        print(" ".join(["-" for x in range(len(self.grid))]))

    def setblock(self, x, y):
        self.grid[y][x] = Object(1)

    def range(self):
        for x in range(self.width):
            for y in range(self.height):
                obj = self.grid[y][x]
                try:
                    if x == 0:
                        if self.grid[y][x+self.width-1].type == 1:
                            obj.nearby += 1
                    elif not x == 0:
                        if self.grid[y][x-1].type == 1:
                            obj.nearby += 1
                except:
                    print("A")
                    pass
                try:
                    if x == 0 and not y == self.height-1:
                        if self.grid[y+1][x+self.width-1].type == 1:
                            obj.nearby += 1
                    elif not x == 0 and y == self.height-1:
                        if self.grid[y-(self.height-1)][x-1].type == 1:
                            obj.nearby += 1
                    elif x == 0 and y == self.height-1:
                        if self.grid[y-(self.height-1)][x+self.width-1].type == 1:
                            obj.nearby += 1
                    elif not x == 0 and not y == self.height-1:
                        if self.grid[y+1][x-1].type == 1:
                            obj.nearby += 1
                except:
                    print("B")
                    pass
                try:
                    if y == self.height-1:
                        if self.grid[y-(self.height-1)][x].type == 1:
                            obj.nearby += 1
                    elif not y == self.height-1:
                        if self.grid[y+1][x].type == 1:
                            obj.nearby += 1
                except:
                    print("C")
                    pass
                try:
                    if x == self.width-1 and y == self.height-1:
                        if self.grid[y-(self.height-1)][x-(self.width-1)].type == 1:
                            obj.nearby += 1
                    elif x == self.width-1 and not y == self.height-1:
                        if self.grid[y+1][x-(self.width-1)].type == 1:
                            obj.nearby += 1
                    elif not x == self.width-1 and y == self.height-1:
                        if self.grid[y-(self.height-1)][x+1].type == 1:
                            obj.nearby += 1
                    elif not x == self.width-1 and not y == self.height-1:
                        if self.grid[y+1][x+1].type == 1:
                            obj.nearby += 1
                except:
                    print("D")
                    pass
                try:
                    if x == self.width-1:
                        if self.grid[y][x-(self.width-1)].type == 1:
                            obj.nearby += 1
                    elif not x == self.width-1:
                        if self.grid[y][x+1].type == 1:
                            obj.nearby += 1
                except:
                    print("E")
                    pass
                try:
                    if x == self.width-1 and y == 0:
                        if self.grid[y+self.height-1][x-(self.width-1)].type == 1:
                            obj.nearby += 1
                    elif x == self.width-1 and not y == 0:
                        if self.grid[y-1][x-(self.width-1)].type == 1:
                            obj.nearby += 1
                    elif not x == self.width-1 and y == 0:
                        if self.grid[y+self.height-1][x+1].type == 1:
                            obj.nearby += 1
                    elif not x == self.width-1 and not y == 0:
                        if self.grid[y-1][x+1].type == 1:
                            obj.nearby += 1
                except:
                    print("F")
                    pass
                try:
                    if y == 0:
                        if self.grid[y+self.height-1][x].type == 1:
                            obj.nearby += 1
                    elif not y == 0:
                        if self.grid[y-1][x].type == 1:
                            obj.nearby += 1
                except:
                    print("G")
                    pass
                try:
                    if x == 0 and y == 0:
                        if self.grid[y+self.height-1][x+self.width-1].type == 1:
                            obj.nearby += 1
                    elif x == 0 and not y == 0:
                        if self.grid[y-1][x+self.width-1].type == 1:
                            obj.nearby += 1
                    elif not x == 0 and y == 0:
                        if self.grid[y+self.height-1][x-1].type == 1:
                            obj.nearby += 1
                    elif not x == 0 and not y == 0:
                        if self.grid[y-1][x-1].type == 1:
                            obj.nearby += 1
                except:
                    print("H")
                    pass

    def locate(self, obj):
        for y in range(self.width):
            for x in range(self.height):
                if obj == self.grid[y][x]:
                    return (x, y)
        return None

class Object():
    def __init__(self, type = 0):
        self.nearby = 0
        self.type = type
