import os
import sys
import time

def can_go_down(grid, x, y):
    if x < len(grid) - 1 and grid[x+1][y] == ".":
        return True
    elif x < len(grid) - 1 and (grid[x+1][y] == "#" or grid[x+1][y] == "o"):
        return False

def can_go_down_left(grid, x, y):
    if x < len(grid) - 1  and grid[x+1][y-1] == ".":
        return True
    elif x < len(grid) - 1  and (grid[x+1][y] == "#" or grid[x+1][y] == "o"):
        return False

def can_go_down_right(grid, x, y):
    if x < len(grid) - 1 and y < len(grid[0]) - 1 and grid[x+1][y+1] == ".":
        return True
    elif x < len(grid) - 1 and y < len(grid[0]) - 1 and (grid[x+1][y] == "#" or grid[x+1][y] == "o"):
        return False

def next_sand(grid, x, y):
    sand = [(x, y)]
    last = None
    times = 0
    while sand:
        times += 1
        # os.system("clear")
        # os.system("clear")
        i,j = sand.pop()
        
        d = can_go_down(grid, i, j)
        dl = can_go_down_left(grid, i, j)
        dr = can_go_down_right(grid, i, j)

        if d:
            if grid[i][j] == "o":
                grid[i][j] = "."
            grid[i+1][j] = "o"
            last = (i+1, j)
            sand.append((i+1, j))
        elif dl:
            if grid[i][j] == "o":
                grid[i][j] = "."
            grid[i+1][j-1] = "o"
            last = (i+1, j-1)
            sand.append((i+1, j-1))
        elif dr:
            if grid[i][j] == "o":
                grid[i][j] = "."
            grid[i+1][j+1] = "o"
            last = (i+1, j+1)
            sand.append((i+1, j+1))
        else:
            if grid[x+1][y] != "o" or grid[x+1][y-1] != "o" or grid[x+1][y+1] != "o":
                sand.append((x, y))
            else:
                grid[x][y] = "o"
        # else:
        #     grid[last[0]][last[1]] = "."
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         print(grid[i][j], end="")
        #     print()

        # if times < 190:
        # time.sleep(0.01)
        # else:
        #     time.sleep(1)

with open("input.txt") as f:
    lines = f.read().splitlines()

    paths = []

    for line in lines:
        path = line.split(" -> ")
        paths.append(path)
    
    min_x, min_y = float("inf"), float("inf")
    max_x, max_y = -float("inf"), -float("inf")

    for path in paths:
        for point in path:
            x, y = point.split(",")
            x, y = int(x), int(y)
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    max_y += 2
    min_x = min(min_x, 500-max_y-1)
    max_x = max(max_x, 500+max_y+1)

    sand_dropper = (0,  500-min_x)

    grid = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y + 1)]

    for path in paths:
        for i in range(len(path)-1):
            x1, y1 = path[i].split(",")
            x2, y2 = path[i+1].split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            x1 -= min_x
            x2 -= min_x

            if x1 == x2:
                if y1 < y2:
                    for y in range(y1, y2+1):
                        grid[y][x1] = "#"
                else:
                    for y in range(y1, y2-1, -1):
                        grid[y][x1] = "#"
            else:
                if x1 < x2:
                    for x in range(x1, x2+1):
                        grid[y1][x] = "#"
                else:
                    for x in range(x1, x2-1, -1):
                        grid[y1][x] = "#"

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == len(grid) - 1:
                for j in range(len(grid[i])):
                    grid[i][j] = "#"
    
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         print(grid[i][j], end="")
    #     print()

    next_sand(grid, sand_dropper[0], sand_dropper[1])

    print(sum([row.count("o") for row in grid]))