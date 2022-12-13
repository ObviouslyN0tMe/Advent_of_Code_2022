# puzzle input
with open("input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)


def adjustTail(head, tail):
    diff_x = head.x - tail.x
    diff_y = head.y - tail.y
    if abs(diff_x) == abs(diff_y) == 2:
        return Coordinate(head.x - diff_x//2, head.y - diff_y//2)
    elif abs(diff_x) == 2:
        return Coordinate(head.x - diff_x//2, head.y)
    elif abs(diff_y) == 2:
        return Coordinate(head.x, head.y - diff_y//2)
    else:
        return tail


movement_dict = {"L": Coordinate(-1, 0), "R": Coordinate(1, 0), "U": Coordinate(0, 1), "D": Coordinate(0, -1)}

knots = []
for i in range(10):
    knots.append(Coordinate(0, 0))

tail_positions_part1 = {(0, 0): True}
tail_positions_part2 = {(0, 0): True}

for line in rawdata:
    move = line.split(" ")
    for i in range(int(move[1])):
        knots[0] += movement_dict[move[0]]
        for knot in range(1, len(knots)):
            knots[knot] = adjustTail(knots[knot - 1], knots[knot])
        tail_positions_part1[(knots[1].x, knots[1].y)] = True
        tail_positions_part2[(knots[-1].x, knots[-1].y)] = True

print(tail_positions_part2)
print("Part 1", len(tail_positions_part1))
print("Part 2", len(tail_positions_part2))
