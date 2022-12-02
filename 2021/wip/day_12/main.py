values = []

with open('ex.txt') as f:
#with open('input.txt') as f:
    for line in f:
        temp_list = []
        line = line.strip().split(" ")
        p1 = line[0].split(',')
        p2 = line[2].split(',')
        temp_list.append(p1)
        temp_list.append(p2)
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