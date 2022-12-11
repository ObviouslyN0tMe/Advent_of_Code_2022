# puzzle input
with open("input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]

x = rawdata.index("")
picture = rawdata[0:x-1]
instructions = rawdata[x+1:]
stacks = {}
stacks_part2 = {}
stack_amount = int(rawdata[x-1][-1])

for stack_nr in range(1, stack_amount + 1):
    stack = []
    for row in picture:
        stack.append(row[1+4*(stack_nr-1):2+4*(stack_nr-1)])
    stack.reverse()
    while stack[-1] in ["", " "]:
        stack.pop(-1)
    stacks[stack_nr] = list(stack)
    stacks_part2[stack_nr] = list(stack)


def moveOneCrate(start, end):
    crate = stacks[start].pop(-1)
    stacks[end].append(crate)


def moveMultipleCrates(start, end, height):
    crates = stacks_part2[start][-height:]
    stacks_part2[start] = stacks_part2[start][0:-height]
    stacks_part2[end] += crates


for line in instructions:
    instruction = line.split(" ")
    amount = int(instruction[1])
    stack_a = int(instruction[3])
    stack_b = int(instruction[5])
    for nr in range(amount):
        moveOneCrate(stack_a, stack_b)
    moveMultipleCrates(stack_a, stack_b, amount)

top_row_part1 = ""
top_row_part2 = ""

print(stacks_part2)

for stack in stacks.values():
    top_row_part1 += stack[-1]

for stack in stacks_part2.values():
    top_row_part2 += stack[-1]

print("Part 1:", top_row_part1)
print("Part 2:", top_row_part2)
