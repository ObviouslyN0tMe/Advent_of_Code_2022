import operator
# puzzle input
with open("input") as file:
    rawdata = [x.strip("\n") for x in file.readlines()]


# monkey class
class Monkey:
    def __init__(self, nr, itemlist, inspect_operator, inspect_value, test_divisor, true_monkey_nr, false_monkey_nr):
        self.number = nr
        self.items = []
        for item in itemlist:
            self.items.append(int(item))
        self.inspect_operator = inspect_operator
        self.inspect_value = inspect_value
        self.test_divisor = test_divisor
        self.true_monkey_nr = true_monkey_nr
        self.false_monkey_nr = false_monkey_nr
        self.total_inspections = 0

    def inspectItems(self):
        inspected_items = []
        for item in self.items:
            self.total_inspections += 1
            item = self.inspect_operator(item, self.inspect_value)
            inspected_items.append(item)
        self.items = inspected_items

    def relief(self):
        inspected_items = []
        for item in self.items:
            item //= 3
            inspected_items.append(item)
        self.items = inspected_items

    def throwItems(self):
        thrown_items = {self.true_monkey_nr: [], self.false_monkey_nr: []}
        for item in self.items:
            if item % self.test_divisor:
                thrown_items[self.false_monkey_nr].append(item)
            else:
                thrown_items[self.true_monkey_nr].append(item)
        return thrown_items

    def catchItems(self, catched_items):
        self.items += catched_items


# prep for formatting input
monkeys = []
monkey_attributes = []
analysed_monkeys = []
operators = {"+": operator.add, "*": operator.mul}

# formatting input
for line in rawdata:
    if line == "":
        monkeys.append(monkey_attributes)
        monkey_attributes = []
    else:
        attribute = line.split(":")
        if attribute[1]:
            monkey_attributes.append(attribute[1])
        else:
            monkey_attributes.append(attribute[0][-1])


# creating monkey objects
for attributes in monkeys:
    inspect_operation = attributes[2].split(" ")
    attribute_inspect_value = inspect_operation[-1]
    if attribute_inspect_value == "old":
        attribute_inspect_value = 2
        attribute_inspect_operator = operator.mul
    else:
        attribute_inspect_operator = operators[inspect_operation[-2]]
    monkey = Monkey(attributes[0], attributes[1].split(", "), attribute_inspect_operator, attribute_inspect_value,
                    attributes[3].split(" ")[-1], attributes[4].split(" ")[-1], attributes[5].split(" ")[-1])
    analysed_monkeys.append(monkey)

# monkeys playing their game
for i in range(20):
    for monkey in analysed_monkeys:
        monkey.inspectItems()
        monkey.relief()
        items_to_catch = monkey.throwItems()
        for catcher, items in items_to_catch.items():
            analysed_monkeys[catcher].catchItems(items)

# check for monkey business
monkey_activity = []
for monkey in analysed_monkeys:
    monkey_activity.append(monkey.total_inspections)
monkey_activity.sort()
monkey_business = monkey_activity[-1] * monkey_activity[-2]
print("Part 1:", monkey_business)