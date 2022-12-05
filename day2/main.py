scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}

wins_with = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

loses_with = {v: k for k, v in wins_with.items()}

with open("input.txt") as f:
    data = f.read().splitlines()
    points = 0
    for line in data:
        player1, result = line.split(" ")
        if result == 'X':  # opponent wins
            points += scores[wins_with[player1]]
        elif result == 'Y':  # tie
            points += scores[player1] + 3
        else:  # i win
            points += scores[loses_with[player1]] + 6
    print(points)
