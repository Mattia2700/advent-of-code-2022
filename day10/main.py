with open("/home/mattiafranzin/Desktop/aoc2022/day10/input.txt") as f:

    cycles_time = {
        'addx': 2,
        'noop': 1
    }

    cycle_number = 1
    timeout = []
    value = 1

    lines = f.read().splitlines()

    for line in lines:
        if line == 'noop':
            timeout.append((0, 1))
        else:
            op = int(line.split(' ')[1])
            timeout.append((op, 2))

    signal = 0
    to_do = None
    doing = False
    
    image = [['.' for i in range(40)] for j in range(6)]

    sprite = [0, 1, 2]

    while len(timeout) > 0:

        row = cycle_number//40
        col = cycle_number%40 - 1

        if col in sprite:
            image[row][col] = '#'

        if not doing:
            to_do = timeout.pop(0)
            doing = True if to_do[1] > 1 else False
        else:
            doing = False
            value += to_do[0]
            sprite = [value-1, value, value+1]

        cycle_number += 1
        

        # if (cycle_number-20)%40 == 0:
        #         signal += cycle_number*value
        #         print("Signal:", signal, "Cycle:", cycle_number, "Value:", value)

    for i in range(len(image)):
        for j in range(len(image[i])):
            print(image[i][j], end="")
        print()
    # print(signal)
