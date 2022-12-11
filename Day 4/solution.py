# puzzle input
with open("input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]

assignment_list = []

# format data
for line in rawdata:
    pair = line.split(",")
    elf1 = pair[0].split("-")
    elf2 = pair[1].split("-")
    assignment_list.append((elf1, elf2))

# calc overlap
fully_contains = 0
overlap_at_all = 0

for pair in assignment_list:
    elf1 = pair[0]
    elf2 = pair[1]
    diff0 = int(elf1[0]) - int(elf2[0])
    diff1 = int(elf1[1]) - int(elf2[1])
    overlap = diff0 * diff1
    if overlap <= 0:
        fully_contains += 1
    if int(elf1[0]) <= int(elf2[1]) and int(elf2[0]) <= int(elf1[1]):
        overlap_at_all += 1

print(rawdata)
print(str(fully_contains), "times one assignments fully contains the other.")
print(str(overlap_at_all), "times one assignments overlaps with the other.")
