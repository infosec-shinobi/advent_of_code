values = []

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        temp_list = []
        line = line.strip()
        first_split = line.split(",")
        for item in first_split:
            second_split = item.split("-")
            temp_list.append(second_split)
        values.append(temp_list)

##########
# Part 1 #
##########
total = 0

for item in values:
    one_low = int(item[0][0])
    one_high = int(item[0][1])
    two_low = int(item[1][0])
    two_high = int(item[1][1])

    if one_low <= two_low and one_high >= two_high:
        total += 1
    elif two_low <= one_low and two_high >= one_high:
        total += 1
    else:
        pass
print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0

for item in values:
    one_range = range(int(item[0][0]), int(item[0][1])+1)
    two_range = range(int(item[1][0]), int(item[1][1])+1)

    for numbr in one_range:
        if numbr in two_range:
            total_2 += 1
            break
print(f'Part 2: {total_2}')