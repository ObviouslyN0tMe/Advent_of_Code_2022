# puzzle input
with open("input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()] + [""]

# setup
carried_calories = []
calories = 0
elf = 0

# calories carry list
for line in rawdata:
    if line:
        print(line)
        calories += int(line)
    else:
        print(line)
        elf += 1
        carried_calories.append((calories, "#" + str(elf)))
        calories = 0

# highest calories and the carrying elfs
carried_calories.sort()
highest_calories = carried_calories[-1][0]
total_three_highest_calories = carried_calories[-1][0] + carried_calories[-2][0] + carried_calories[-3][0]
elfs_to_ask = carried_calories[-1][1] + ", " + carried_calories[-2][1] + " and " + carried_calories[-3][1]

# Part 1
print("Elf to ask is", str(carried_calories[-1][1]), "and he carries", str(highest_calories), "calories.")

# Part 2
print("The 3 Elfs to ask are ", elfs_to_ask + ". Together they carry", str(total_three_highest_calories), "calories.")
