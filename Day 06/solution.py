# puzzle input
with open("input") as file:
    rawdata = file.readline().strip("\n")

print(rawdata)


def solution(string_length):
    for x in range(0, len(rawdata) - 4):
        string = list(rawdata[x + 0: x + string_length])
        repeat = False
        for letter in string:
            if string.count(letter) > 1:
                repeat = True
        if not repeat:
            return x + string_length


part1 = solution(4)
part2 = solution(14)

print("Part 1:", part1)
print("Part 2:", part2)