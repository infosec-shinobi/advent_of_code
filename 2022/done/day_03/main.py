def value_lookup(numbr):
    
    #Lowercase item types a through z have priorities 1 through 26. (ord - 96)
    #Uppercase item types A through Z have priorities 27 through 52. (ord - 38)
    u_case = numbr.isupper()
    if u_case:
        return (ord(numbr)-38)
    else:
        return (ord(numbr)-96)


values = []

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        values.append(line)

##########
# Part 1 #
##########
total = 0
new_list = []
for item in values:
    front = item[:(len(item)//2)]
    back = item[(len(item)//2):]
    temp_list = [front, back]

    duped_items = ""
    for letter in front:
        if letter in back:
            if letter in duped_items:
                pass
            else:
                duped_items += letter
        else:
            pass
    temp_list.append(duped_items)
    new_list.append(temp_list)

for things in new_list:
    check_value = things[2]
    total += value_lookup(check_value)

print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0
count = 0
elf_groups = []
temp_list = []
for item in values:
    if count < 3:
        temp_list.append(item)
        count += 1
    else:
        elf_groups.append(temp_list)
        count = 1
        temp_list = []
        temp_list.append(item)
elf_groups.append(temp_list)

card_tracker = []

for group in elf_groups:
    elf1 = group[0]
    elf2 = group[1]
    elf3 = group[2]

    for thing in elf1:
        if thing in elf2:
            if thing in elf3:
                card_tracker.append(thing)
                break

for card in card_tracker:
    total_2 += value_lookup(card)

print(f'Part 2: {total_2}')