# https://adventofcode.com/2021/day/1
# --- Day 1: Sonar Sweep ---

def sum_list(list_of_nums):
    total = 0
    for item in list_of_nums:
        total += item
    return total

values = []

with open('input.txt') as f:
    for line in f:
        line = int(line.strip())
        values.append(line)

##########
# Part 1 #
##########

first_num = True
increase_count = 0
previous_value = 0
current_value = 0

for item in values:
    if first_num:
        previous_value = item
        first_num = False
    else:
        current_value = item
        if current_value > previous_value:
            increase_count+=1
        previous_value = current_value

print(f'Part 1: {increase_count}')

##########
# Part 2 #
##########

cur = 0
old = 0
cur_list = []
old_list = []
increase_win = 0

count = 0

for num in range(0,len(values)):
    if count < 3:
        count+=1
    elif count == 3:
        old_list= [values[num-2],values[num-1],values[num]]
        old = sum_list(old_list)
        count += 1
    else:
        cur_list= [values[num-2],values[num-1],values[num]]
        cur = sum_list(cur_list)
        if cur > old:
            increase_win+=1
        old = cur
print(f'Part 2: {increase_win}')