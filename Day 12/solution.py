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
                if self.coordinates[coordinate] - self.coordinates[neighbour] <= 1:
                    self.paths[neighbour].append(coordinate)
                if self.coordinates[neighbour] - self.coordinates[coordinate] <= 1:
                    self.paths[coordinate].append(neighbour)


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


# find shortest route part 1
def findShortestRoute(startpoint):
    distances = {startpoint: 0}
    to_be_checked_now = [startpoint]
    to_be_checked_next = []
    end = special_coords["E"]
    while to_be_checked_now:
        for route_start in to_be_checked_now:
            distance = distances[route_start] + 1
            for route_end in heightmap.paths[route_start]:
                if route_end not in distances:
                    distances[route_end] = distance
                    to_be_checked_next.append(route_end)
        to_be_checked_now = to_be_checked_next
        to_be_checked_next = []
    if end in distances:
        return distances[end]
    else:
        return False


shortest_distance = findShortestRoute(special_coords["S"])
print("Part 1:", shortest_distance)

# find shortest route part 2
for startpoint_a, height in heightmap.coordinates.items():
    if height == 0:
        distance = findShortestRoute(startpoint_a)
        if distance and distance < shortest_distance:
            shortest_distance = distance

print("Part 2:", shortest_distance)
