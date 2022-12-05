with open("input.txt") as f:
    lines = f.read().splitlines()
    sum = 0
    groups = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    for group in groups:
        common = list(dict.fromkeys([c for c in group[0] if c in group[1] and c in group[2]])).pop()
        if common.isupper():
            sum += ord(common) - ord('A') + 26 + 1
        else:
            sum += ord(common) - ord('a') + 1
    print(sum)