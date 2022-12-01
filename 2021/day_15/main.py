values = []

with open('ex.txt') as f:
#with open('input.txt') as f:
    for line in f:
        line = line.strip()
        temp_list = []
        for item in line:
            temp_list.append(int(item))
        values.append(temp_list)

print(values)

##########
# Part 1 #
##########
total = 0
row_count = len(values)-1
row_length = len(values[0])-1
goal ={"row":row_count, "position":row_length}
current_least_risk = 0


##########
# Part 2 #
##########
part_2_total = 0

print(f'Part 2: {part_2_total}')