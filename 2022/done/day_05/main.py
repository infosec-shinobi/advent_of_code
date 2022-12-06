import copy

crates = []
instructs = []
rows = []

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        line =  line.strip("\n")
        if "[" in line:
            crates.append(line)
        elif "move" in line:
            instructs.append(line)
        elif line.strip() == "":
            pass
        else:
            rows = line.strip().split()

#print(crates, instructs, rows)
##########
# Part 1 #
##########
total = ""
master_tracker = {}
total_rows = len(rows)

for row in rows:
    master_tracker[row] = ""

for crate in crates:
    count = 1
    temp_list = crate[1::4]
    for item in temp_list:
        if item == " ":
            pass
        else:
            master_tracker[str(count)] = master_tracker[str(count)] + item
        count +=1

master_tracker2 = copy.deepcopy(master_tracker)

for steps in instructs:
    steps = steps.split(" ")
    move = steps[1]
    move_from = steps[3]
    move_to = steps[5]

    move_from_value = list(master_tracker[move_from])
    move_to_value = list(master_tracker[move_to])
    x = range(0,int(move))

    for y in x:
        removed_item = move_from_value.pop(0)
        move_to_value.insert(0, removed_item)
    
    master_tracker[move_from] = move_from_value
    master_tracker[move_to] = move_to_value

for x in master_tracker.values():
    total += x[0]

print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = ""

for steps in instructs:
    steps = steps.split(" ")
    move = steps[1]
    move_from = steps[3]
    move_to = steps[5]

    move_from_value = list(master_tracker2[move_from])
    move_to_value = list(master_tracker2[move_to])
    x = range(0,int(move))
    removed_items = []

    for y in x:
        removed_items.append(move_from_value.pop(0))
    
    removed_items.extend(move_to_value)
    
    master_tracker2[move_from] = move_from_value
    master_tracker2[move_to] = removed_items

for x in master_tracker2.values():
    total_2 += x[0]

print(f'Part 2: {total_2}')