# puzzle input
with open("input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]

# variables
games1 = []
games2 = []
outcome = {0: 3, 1: 6, 2: 0}

# format games
# part 1
for line in rawdata:
    line = line.replace("A", "0")
    line = line.replace("B", "1")
    line = line.replace("C", "2")
    line = line.replace(" X", "0")
    line = line.replace(" Y", "1")
    line = line.replace(" Z", "2")
    games1.append((int(line[0]), int(line[1])))

# part 2
for line in rawdata:
    line = line.replace("A", "0")
    line = line.replace("B", "1")
    line = line.replace("C", "2")
    if "X" in line:
        games2.append((int(line[0]), (int(line[0]) - 1) % 3))
    elif "Y" in line:
        games2.append((int(line[0]), int(line[0])))
    else:
        games2.append((int(line[0]), (int(line[0]) + 1) % 3))


# calc score
def calc_score(games):
    score = 0
    for game in games:
        score += game[1] + 1
        diff = game[1] - game[0]
        if diff < 0:
            diff += 3
        score += outcome[diff]
    return score


# output
print("Part 1 Score:", calc_score(games1))
print("Part 2 Score:", calc_score(games2))

