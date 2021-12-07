def next_day(current_fish_list):

    new_fish_count = 0
    temp_list = []

    for fish in current_fish_list:
        if fish > 0:
            temp_list.append(fish-1)
        else:
            temp_list.append(6)
            new_fish_count +=1
    while new_fish_count > 0:
        temp_list.append(8)
        new_fish_count -=1
    
    return temp_list

def p2_next_day(current_fish_dict):

    updated_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    
    for key, value in current_fish_dict.items():
        if key == 0:
            updated_dict[6] += value
            updated_dict[8] += value
        else:
            updated_dict[key-1] += value
    return updated_dict

values = []

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip().split(",")
    for num in line:
        values.append(int(num))

fish_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for item in values:
    fish_dict[item] += 1

##########
# Part 1 #
##########

day_count = 0

while day_count < 80:
#while day_count < 18:
    values = next_day(values)
    day_count +=1

print(f'Part 1: {len(values)}')

##########
# Part 2 #
##########

day_count = 0

while day_count < 256:
#while day_count < 18:
    fish_dict = p2_next_day(fish_dict)
    day_count +=1

p2_total = 0
for key, value in fish_dict.items():
    p2_total += value

print(f'Part 2: {p2_total}')