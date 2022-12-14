import ast
# puzzle input
with open("testinput") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]


def comparePackets(packet1, packet2):
    while packet1 and packet2:
        element1 = packet1[0]
        element2 = packet2[0]
        # make both elements the same type
        if type(element1) == list or type(element2) == list:
            if type(element1) == int:
                element1 = [element1]
            if type(element2) == int:
                element2 = [element2]
            # new comparison of 2 lists
            comparison = comparePackets(element1, element2)
            if comparison == "equal":
                packet1.pop(0)
                packet2.pop(0)
            else:
                return comparison
        elif element1 != element2:
            return element1 < element2
        else:
            packet1.pop(0)
            packet2.pop(0)
    if packet1:
        return False
    elif packet2:
        return True
    else:
        return "equal"

def compare(left, right):
    if type(left) == int and type(right) == int:
        return left < right
    if len(left) == 0:
        return True
    if len(right) == 0:
        return False
    else:
        leftElement = left.pop(0)
        rightElement = right.pop(0)
        if type(leftElement) == list or type(rightElement) == list:
            leftElement = leftElement if type(leftElement) == list else [leftElement]
            rightElement = rightElement if type(rightElement) == list else [rightElement]

        if compare(leftElement, rightElement):
            return True
        elif compare(rightElement, leftElement):
            return False
        else:
            return compare(left, right)


packet_1 = ""
packet_2 = ""
pair_index = 0
sum_of_indices = 0

for line in rawdata:
    if line:
        packet_1 = packet_2
        packet_2 = ast.literal_eval(line)
    else:
        pair_index += 1
        print(packet_1)
        print(packet_2)
        if compare(packet_1, packet_2):
            sum_of_indices += pair_index
            print(True)
        else:
            print(False)

print("Part 1:", sum_of_indices)
