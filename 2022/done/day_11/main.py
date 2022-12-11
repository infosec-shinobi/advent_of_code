import math
import copy

class Monkey:
    def __init__(self, monkey_num, items, ops, test_num, true_num, false_num):
        self.monkey_num = monkey_num
        self.items = items
        self.ops = ops
        self.test_num = test_num
        self.true_num = true_num
        self.false_num = false_num
        self.inspect_count = 0

    def operation(self, worry_level):
        old = worry_level
        self.inspect_count +=1
        return eval(self.ops, {"old": old})

    def bored(self, worry_level):
        return (math.floor(worry_level/3))

    def test(self, worry_level):
        if worry_level%self.test_num == 0:
            return self.true_num
        else:
            return self.false_num

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)

monkey_tracker = {}
divisors = []
#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if "Monkey" in line:
            monkey_num = int(line.split(":")[0].split()[1])
        elif "Starting" in line:
            items = line.split(": ")[1].split(", ")
            temp_list = []
            for item in items:
                temp_list.append(int(item))
            items = temp_list
        elif "Operation" in line:
            ops = line.split("= ")[1].split()
            ops = " ".join(ops)
        elif "Test" in line:
            test_num = int(line.split("by ")[1])
            divisors.append(test_num)
        elif "true" in line:
            true_num = int(line.split("monkey ")[1])
        elif "false" in line:
            false_num = int(line.split("monkey ")[1])
        else:
            monkey_tracker[monkey_num] = Monkey(monkey_num, items, ops, test_num, true_num, false_num)

monkey_tracker[monkey_num] = Monkey(monkey_num, items, ops, test_num, true_num, false_num)

pt2_monkey_tracker = copy.deepcopy(monkey_tracker)

##########
# Part 1 #
##########

for round in range(1,21):
    for monkey in range(0,len(monkey_tracker.keys())):
        current_items = list(monkey_tracker[monkey].items)
        for item in current_items:
            current_worry = monkey_tracker[monkey].operation(item)
            current_worry = monkey_tracker[monkey].bored(current_worry)
            new_owner = monkey_tracker[monkey].test(current_worry)
            monkey_tracker[monkey].remove_item(item)
            monkey_tracker[new_owner].add_item(current_worry)

total = 0
inspections = []
for k,v in monkey_tracker.items():
    inspections.append(v.inspect_count)
inspections.sort()
total = inspections[-1]*inspections[-2]
    
print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0
lcm = 1
for num in range(0, len(divisors)):
    lcm = math.lcm(lcm, divisors[num])

for round in range(1,10001):
    for monkey in range(0,len(pt2_monkey_tracker.keys())):
        current_items = list(pt2_monkey_tracker[monkey].items)
        for item in current_items:
            current_worry = pt2_monkey_tracker[monkey].operation(item)
            current_worry %= lcm
            new_owner = pt2_monkey_tracker[monkey].test(current_worry)
            pt2_monkey_tracker[monkey].remove_item(item)
            pt2_monkey_tracker[new_owner].add_item(current_worry)

pt2_inspections = []

for k,v in pt2_monkey_tracker.items():
    pt2_inspections.append(v.inspect_count)

pt2_inspections.sort()
total_2 = pt2_inspections[-1]*pt2_inspections[-2]
print(f'Part 2: {total_2}')