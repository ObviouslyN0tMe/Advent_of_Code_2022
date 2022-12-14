# puzzle input
with open("input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]


class Map:
    def __init__(self):
        self.coordinates = {}
        self.paths = {}

    def addCoordinate(self, coordinate: tuple, height: int):
        self.coordinates[coordinate] = height
        neighbours = [(coordinate[0], coordinate[1] + 1), (coordinate[0], coordinate[1] - 1),
                      (coordinate[0] + 1, coordinate[1]), (coordinate[0] - 1, coordinate[1])]
        self.paths[coordinate] = []
        for neighbour in neighbours:
            if neighbour in self.coordinates:
                if abs(self.coordinates[coordinate] - self.coordinates[neighbour]) <= 1:
                    self.paths[coordinate].append(neighbour)
                    self.paths[neighbour].append(coordinate)


heightmap = Map()
special_coords = {"S": 0, "E": 25}

# format data
for y, line in enumerate(rawdata):
    for x, letter in enumerate(line):
        height_lvl = ord(letter) - 97
        if height_lvl >= 0:
            heightmap.addCoordinate((x, y), height_lvl)
        else:
            heightmap.addCoordinate((x, y), special_coords[letter])
            special_coords[letter] = (x, y)

# find shortest route
distances = {special_coords["S"]: 0}
next_step = [special_coords["S"]]
to_be_checked = []
end = special_coords["E"]
while end not in distances:
    for route_start in next_step:
        distance = distances[route_start]
        for route_end in heightmap.paths[route_start]:
            if route_end not in distances:
                distances[route_end] = distance + 1
                to_be_checked.append(route_end)
    next_step = to_be_checked
    to_be_checked = []

print(distances[end])

for y in range(5):
    line = ""
    for x in range(8):
        if (x, y) in distances:
            line += "{:03d}".format(distances[(x, y)])
        else:
            line += "xx"
        line += "_"
    print(line)
