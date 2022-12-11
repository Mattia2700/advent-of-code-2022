# with open("input.txt") as f:
#     data = f.read().splitlines()
#     horizontal = 0
#     horizontal_max = -float("inf")
#     horizontal_min = 0
#     vertical = 0
#     vertical_max = -float("inf")
#     vertical_min = 0
#     for line in data:
#         direction, distance = line.split(" ")
#         if direction == "R":
#             horizontal += int(distance)
#             if horizontal > horizontal_max:
#                 horizontal_max = horizontal
#             if horizontal < horizontal_min:
#                 horizontal_min = horizontal
#         elif direction == "L":
#             horizontal -= int(distance)
#             if horizontal > horizontal_max:
#                 horizontal_max = horizontal
#             if horizontal < horizontal_min:
#                 horizontal_min = horizontal
#         elif direction == "U":
#             vertical -= int(distance)
#             if vertical > vertical_max:
#                 vertical_max = vertical
#             if vertical < vertical_min:
#                 vertical_min = vertical
#         elif direction == "D":
#             vertical += int(distance)
#             if vertical > vertical_max:
#                 vertical_max = vertical
#             if vertical < vertical_min:
#                 vertical_min = vertical
    
#     if horizontal_max < 0:
#         horizontal_max = 0
#     if vertical_max < 0:
#         vertical_max = 0

#     print("Horizontal: ", horizontal_min, horizontal_max)
#     print("Vertical: ", vertical_min, vertical_max)

#     grid = [[0 for i in range(horizontal_max + 1)] for j in range(vertical_max + 1)]

import math

def add_position(t, positions):
    if t not in positions:
        positions.append(t)

def directions(h,t):
    # print("Head in", h, "Tail in", t, end=" ")
    if h[0] - t[0] == 1 and h[1] - t[1] == 2 or h[0] - t[0] == 2 and h[1] - t[1] == 1 or h[0] - t[0] == 2 and h[1] - t[1] == 2:
        return (t[0]+1, t[1]+1)
    elif h[0] - t[0] == 1 and h[1] - t[1] == -2 or h[0] - t[0] == 2 and h[1] - t[1] == -1 or h[0] - t[0] == 2 and h[1] - t[1] == -2:
        return (t[0]+1, t[1]-1)
    elif h[0] - t[0] == -1 and h[1] - t[1] == 2 or h[0] - t[0] == -2 and h[1] - t[1] == 1 or h[0] - t[0] == -2 and h[1] - t[1] == 2:
        return (t[0]-1, t[1]+1)
    elif h[0] - t[0] == -1 and h[1] - t[1] == -2 or h[0] - t[0] == -2 and h[1] - t[1] == -1 or h[0] - t[0] == -2 and h[1] - t[1] == -2:
        return (t[0]-1, t[1]-1)
    elif h[0] - t[0] == 2 and h[1] - t[1] == 0:
        return (t[0]+1, t[1])
    elif h[0] - t[0] == -2 and h[1] - t[1] == 0:
        return (t[0]-1, t[1])
    elif h[0] - t[0] == 0 and h[1] - t[1] == 2:
        return (t[0], t[1]+1)
    elif h[0] - t[0] == 0 and h[1] - t[1] == -2:
        return (t[0], t[1]-1)

with open("input.txt") as f:
    data = f.read().splitlines()
    horizontal = 0
    vertical = 0
    positions = []
    body = [(0,0)]*10
    # print(body)
    add_position((0,0), positions)
    for line in data:
        direction, distance = line.split(" ")
        if direction == "R":
            for i in range(int(distance)):
                for j in range(len(body)):
                    if j == 0:
                        body[j] = (body[j][0], body[j][1] + 1)
                        # print(body[j], end=" ")
                        continue
                    distance = math.sqrt((body[j][0] - body[j - 1][0]) ** 2 + (body[j][1] - body[j - 1][1]) ** 2)
                    if distance == 2:
                        body[j] = directions(body[j-1], body[j])
                        if j == len(body) - 1:
                            add_position(body[j], positions)
                    elif distance == math.sqrt(5) or distance == math.sqrt(8):
                        body[j] = directions(body[j-1], body[j])
                        if j == len(body) - 1:
                            add_position(body[j], positions)
                    # print(body[j], end=" ")
                # print()
            # print()
        elif direction == "L":
            for i in range(int(distance)):
                for j in range(len(body)):
                    if j == 0:
                        body[j] = (body[j][0], body[j][1] - 1)
                        # print(body[j], end=" ")
                        continue
                    distance = math.sqrt((body[j][0] - body[j - 1][0]) ** 2 + (body[j][1] - body[j - 1][1]) ** 2)
                    if distance == 2:
                        body[j] = directions(body[j-1], body[j])
                        if j == len(body) - 1:
                            add_position(body[j], positions)
                    elif distance == math.sqrt(5) or distance == math.sqrt(8):
                        body[j] = directions(body[j-1], body[j])
                        if j == len(body) - 1:
                            add_position(body[j], positions)
                    # print(body[j], end=" ")
                # print()
            # print()
        elif direction == "U":
            for i in range(int(distance)):
                for j in range(len(body)):
                    if j == 0:
                        body[j] = (body[j][0] - 1, body[j][1])
                        # print(body[j], end=" ")
                        continue
                    distance = math.sqrt((body[j][0] - body[j - 1][0]) ** 2 + (body[j][1] - body[j - 1][1]) ** 2)
                    if distance == 2:
                        body[j] = directions(body[j-1], body[j])
                        if j == len(body) - 1:
                            add_position(body[j], positions)
                    elif distance == math.sqrt(5) or distance == math.sqrt(8):
                        body[j] = directions(body[j-1], body[j])
                        if j == len(body) - 1:
                            add_position(body[j], positions)
                    # print(body[j], end=" ")
                # print()
            # print()
        elif direction == "D":
            for i in range(int(distance)):
                for j in range(len(body)):
                    if j == 0:
                        body[j] = (body[j][0] + 1, body[j][1])
                        # print(body[j], end=" ") 
                        continue
                    distance = math.sqrt((body[j][0] - body[j - 1][0]) ** 2 + (body[j][1] - body[j - 1][1]) ** 2)
                    if distance == 2:
                        body[j] = directions(body[j-1], body[j])
                        if j == len(body) - 1:
                            add_position(body[j], positions)
                    elif distance == math.sqrt(5) or distance == math.sqrt(8):
                        body[j] = directions(body[j-1], body[j])
                        if j == len(body) - 1:
                            add_position(body[j], positions)
                    # print(body[j], end=" ")
                # print()
            # print()
    
        
    print(len(positions))

        