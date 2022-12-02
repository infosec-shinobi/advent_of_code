def compare_nums(a,b):
    if a < b:
        return True
    else: 
        return False

values = []

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        temp_list = []
        line = line.strip()
        for num in line:
            temp_list.append(num)
        values.append(temp_list)

##########
# Part 1 #
##########

#how many times do digits 1, 4, 7, or 8 appear
# len of 2, 4, 3, 7

depth_of_list = len(values)
len_of_single_list = len(values[0])
total = 0
low_nums = []

for row in range(0,depth_of_list):
    prev_row = []
    next_row = []
    cur_row = values[row]

    if row == 0:
        next_row = values[row+1]
    elif row == (depth_of_list -1):
        prev_row = values[row-1]
    else:
        next_row = values[row+1]
        prev_row = values[row-1]

    for num in range(0, len_of_single_list):
        check_returns = []
        if len(prev_row) != 0: #check above
            check_returns.append(compare_nums(cur_row[num],prev_row[num]))
        if len(next_row) != 0: #check below
            check_returns.append(compare_nums(cur_row[num],next_row[num]))
        if num != 0: # check left
                check_returns.append(compare_nums(cur_row[num],cur_row[num-1]))
        if num != (len_of_single_list - 1): #check right
                check_returns.append(compare_nums(cur_row[num],cur_row[num+1]))

        if False not in check_returns:
            low_nums.append(cur_row[num])
for number in low_nums:
    total += int(number) + 1

print(f'Part 1: {total}')

##########
# Part 2 #
##########

#print(f'Part 2: {increase_win}')