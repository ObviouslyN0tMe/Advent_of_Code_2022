# puzzle input
with open("input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]


class Cpu:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.buffer = 0
        self.signal_strengths = []
        self.pixels = []
        self.functions = {"addx": self.addX, "noop": self.noop}

    def newCycle(self):
        self.cycle += 1
        self.calcSignalStrength()
        self.drawPixel()

    def addX(self, x):
        self.newCycle()
        self.newCycle()
        self.x += int(x)

    def noop(self):
        self.newCycle()

    def calcSignalStrength(self):
        interesting = (self.cycle + 20) % 40
        if not interesting and self.cycle <= 220:
            self.signal_strengths.append(self.cycle*self.x)

    def drawPixel(self):
        current_pixel = self.cycle % 40
        diff = current_pixel - self.x
        if diff in [0, 1, 2]:
            self.pixels.append("#")
        else:
            self.pixels.append(".")


cpu = Cpu()

for line in rawdata:
    instruction = line.split(" ")
    functions = cpu.functions
    if len(instruction) == 2:
        functions[instruction[0]](instruction[1])
    else:
        functions[instruction[0]]()

result = 0
for signal_strength in cpu.signal_strengths:
    result += signal_strength

print("Part 1:", result)
print("Part 2:")
for i in range(6):
    print(cpu.pixels[i*40: i*40 + 39])
