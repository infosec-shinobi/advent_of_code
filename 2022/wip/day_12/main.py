values = []

with open('ex.txt') as f:
#with open('input.txt') as f:
    for line in f:
        temp_list = []
        line = line.strip()
        for num in line:
            temp_list.append(num)
        values.append(temp_list)

##########
# Part 1 #
##########
total = 0

print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0

print(f'Part 2: {total_2}')