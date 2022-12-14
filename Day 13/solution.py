import ast
import functools
# puzzle input
with open("input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]
rawdata.append("")


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
            return element2 - element1
        else:
            packet1.pop(0)
            packet2.pop(0)
    if packet1:
        return -1
    elif packet2:
        return 1
    else:
        return "equal"


# michis variante
def compare(left, right):
    if left == right:
        return "equal"
    if type(left) == int:
        return left < right
    if len(left) == 0:
        return True
    if len(right) == 0:
        return False
    else:
        left_element = left.pop(0)
        right_element = right.pop(0)
        if type(left_element) == list or type(right_element) == list:
            left_element = left_element if type(left_element) == list else [left_element]
            right_element = right_element if type(right_element) == list else [right_element]

        comparison = compare(left_element, right_element)
        if comparison == "equal":
            return compare(left, right)
        else:
            return comparison


packet_1 = ""
packet_2 = ""
pair_index = 0
sum_of_indices = 0
packet_list_part2 = []

for line in rawdata:
    if line:
        packet_list_part2.append(ast.literal_eval(line))
        packet_1 = packet_2
        packet_2 = ast.literal_eval(line)
    else:
        pair_index += 1
        if comparePackets(packet_1, packet_2):
            sum_of_indices += pair_index

print("Part 1:", sum_of_indices)

packet_list_part2 += [[[2]], [[6]]]
packet_list_part2 = sorted(packet_list_part2, key=functools.cmp_to_key(comparePackets))
print("Part 2", packet_list_part2.index([[2]])*packet_list_part2.index([[6]]))