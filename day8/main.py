def scenic_up(grid, i, j):
    value = 1
    for k in range(i-1, 0, -1):
        if grid[k][j] >= grid[i][j]:
            break
        value += 1
    return value

def scenic_down(grid, i, j):
    value = 1
    for k in range(i+1, len(grid)-1):
        if grid[k][j] >= grid[i][j]:
            break
        value += 1
    return value

def scenic_left(grid, i, j):
    value = 1
    for k in range(j-1, 0, -1):
        if grid[i][k] >= grid[i][j]:
            break
        value += 1
    return value

def scenic_right(grid, i, j):
    value = 1
    for k in range(j+1, len(grid[i])-1):
        if grid[i][k] >= grid[i][j]:
            break
        value += 1
    return value

def scenic(grid, i, j):
    # print(scenic_up(grid, i, j))
    # print(scenic_down(grid, i, j))
    # print(scenic_left(grid, i, j))
    # print(scenic_right(grid, i, j))
    # value = scenic_up(grid, i, j) * scenic_down(grid, i, j) * scenic_left(grid, i, j) * scenic_right(grid, i, j)
    # print("the scenic value of ({}, {}) with value {} is {}".format(i, j, grid[i][j], value))
    return scenic_up(grid, i, j) * scenic_down(grid, i, j) * scenic_left(grid, i, j) * scenic_right(grid, i, j)

with open("input.txt") as f:
    lines = f.read().splitlines()
    grid = []
    best = 0
    for line in lines:
        grid.append(list(line))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i==0 or j==0 or i==len(grid)-1 or j==len(grid[i])-1:
                continue
            else:
                best = max(best, scenic(grid, i, j))

    print(best)
    