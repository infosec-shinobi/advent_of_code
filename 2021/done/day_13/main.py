values = []
instructions = []

def fold(fold_axis, fold_line, initial_dict):
    new_dic = {}
    if fold_axis == 'y':
        for x,y in initial_dict:
            if y < fold_line:
                new_dic[(x,y)] = True
            else:
                temp_y = fold_line-(y-fold_line)
                new_dic[(x,temp_y)] = True
    if fold_axis == 'x':
        for x,y in initial_dict:
            if x < fold_line:
                new_dic[(x,y)] = True
            else:
                temp_x = fold_line-(x-fold_line)
                new_dic[(temp_x,y)] = True
    return new_dic

#with open('ex.txt') as f:
with open('input.txt') as f:
    space_hit = False
    for line in f:
        line = line.strip()
        if line == "":
            space_hit = True
        elif space_hit:
            line = line.split("=")
            temp_list = []
            temp_list.append(line[0][-1])
            temp_list.append(line[1])
            instructions.append(temp_list)
        else:
            line = line.split(",")
            values.append(line)

##########
# Part 1 #
##########
total = 0

initial_dict = {}
for item in values:
    initial_dict[(int(item[0]),int(item[1]))] = True

fold_axis = instructions[0][0]
fold_line = int(instructions[0][1])
updated_dict = fold(fold_axis, fold_line, initial_dict)

total = len(updated_dict)
print(f'Part 1: {total}')

instructions.pop(0)

##########
# Part 2 #
##########
part_2_total = 0

for item in instructions:
    fold_axis = item[0]
    fold_line = int(item[1])
    updated_dict = fold(fold_axis, fold_line, updated_dict)

x_values = []
y_values = []
for x,y in updated_dict.keys():
    x_values.append(x)
    y_values.append(y)

sort_x = sorted(x_values)
sort_y = sorted(y_values)

max_x = sort_x[-1]
max_y = sort_y[-1]

final_list = []
for y in range(0,max_y+1):
    temp_string = ""
    for x in range(0,max_x+1):
        if (x,y) in updated_dict:
            temp_string += '#'
        else:
            temp_string += ' '
    final_list.append(temp_string)

print(f'Part 2:')
for line in final_list:
    print(line)