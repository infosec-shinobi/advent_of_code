input_list = []
#with open('ep1.txt') as f:
with open('i.txt') as f:
    for line in f:
        line = line.strip()
        input_list.append(line)

matching_nums = {}

for line in input_list:
    game, data = line.split(": ")
    win_nums, elfs_nums = data.split(" | ")
    win_nums_list = win_nums.split()
    elfs_nums_list = elfs_nums.split()
    matching_nums[game] = sum(winning_num in elfs_nums_list for winning_num in win_nums_list)

total = 0

for _, winning_count in matching_nums.items():
    if int(winning_count) == 1:
        total += 1
    elif int(winning_count) > 1:
        total += 2**(winning_count-1) 
print(f'Part 1: {total}')