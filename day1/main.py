with open("input.txt") as f:
    data = f.read().splitlines()
    sum = 0
    elves = []
    for line in data:
        if line != "":
            sum += int(line)
        else:
            elves.append(sum)
            sum = 0
    elves.sort(reverse=True)
    print(elves[0]+elves[1]+elves[2])
