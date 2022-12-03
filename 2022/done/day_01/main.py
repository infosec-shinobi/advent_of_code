calories_dict = {}
elf_tracker = 1
temp_cals = 0

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line == "":
            calories_dict[elf_tracker] = temp_cals
            elf_tracker += 1
            temp_cals = 0
        else:
            temp_cals += int(line)

##########
# Part 1 #
##########

sorted_list = sorted(calories_dict.values())

print(f'Part 1: {sorted_list[-1]}')

##########
# Part 2 #
##########

top3 = sorted_list[-1] + sorted_list[-2] + sorted_list[-3]

print(f'Part 2: {top3}')