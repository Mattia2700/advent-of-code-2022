import re

with open("input.txt") as f:
    data = f.read()
    # split the data into 2 parts based on the empty line
    config, messages = data.split("\n\n")

    column = {}

    # count how many whitespace characters are in the line before another character
    config = config.splitlines()
    for conf in config:
        whitespaces = 0
        for c in conf:
            if c == " " or c == "[" or c == "]":
                whitespaces += 1
            elif c.isalpha():
                if whitespaces // 4 + 1 not in column:
                    column[whitespaces // 4 + 1] = []
                column[whitespaces // 4 + 1].append(c)    
                whitespaces += 1
    for k,v in column.items():
        column[k] = v[::-1]

    operations = [re.findall(r"move (\d+) from (\d+) to (\d+)", line).pop() for line in messages.splitlines()]

    for op in operations:
        quantity_, from_, to_ = op
        buffer = []
        for i in range(int(quantity_)):
            buffer.append(column[int(from_)].pop())
        buffer = buffer[::-1]
        # append the buffer to the column
        column[int(to_)] += buffer

        # for c in sorted(column.keys()):
        #     print("Elements in " + str(c) + ": " + " ".join([el for el in column[c]]))

    for k in sorted(column.keys()):
        # print without newline
        if column[k] != []:
            print("".join(column[k][-1]), end="")
    print()