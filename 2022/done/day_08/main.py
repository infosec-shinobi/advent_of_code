import math

rows = {}
columns = {}
row_count = 1
overall = {}

def tree_view(tree_height, other_tree_list):
    tree_count = 0
    for x in other_tree_list:
        if tree_height > x:
            tree_count += 1
        else:
            tree_count += 1
            return tree_count
    return tree_count

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        temp_rows = []
        column_count = 1
        line = line.strip()
        for num in line:
            key_value = str(row_count)+str(column_count)
            overall[key_value] = False
            temp_rows.append(num)
            temp_column = columns.get(column_count,[])
            temp_column.append(num)
            columns[column_count] = temp_column
            column_count +=1
        rows[row_count] = temp_rows
        row_count += 1

##########
# Part 1 #
##########
total = 0

r_count = len(rows)
c_count = len(columns)

for x in range(0, r_count):
    if x == 0 or x == r_count-1:
        total += r_count
    else:
        row_data = rows[x+1]
        for y in range(0, c_count):
            column_data = columns[y+1]
            if y == 0 or y == c_count-1:
                total += 1
            else:
                left_max = max(row_data[:y])
                right_max = max(row_data[y+1:])
                up_max = max(column_data[:x])
                down_max = max(column_data[x+1:])
                target = row_data[y]
                if target > left_max or target > right_max or target > up_max or target > down_max:
                    total += 1

print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0

for x in range(0, r_count):
    if x == 0 or x == r_count-1:
        pass
    else:
        row_data = rows[x+1]
        for y in range(0, c_count):
            column_data = columns[y+1]
            if y == 0 or y == c_count-1:
                pass
            else:
                temp_list = []
                left_trees = row_data[:y]
                right_trees = row_data[y+1:]
                up_trees = column_data[:x]
                down_trees = column_data[x+1:]
                target_tree = row_data[y]
                
                temp_list.append(tree_view(target_tree,left_trees[::-1]))
                temp_list.append(tree_view(target_tree,right_trees[::1]))
                temp_list.append(tree_view(target_tree,up_trees[::-1]))
                temp_list.append(tree_view(target_tree,down_trees[::1]))
                temp_total = math.prod(temp_list)

                if temp_total > total_2:
                    total_2 = temp_total

print(f'Part 2: {total_2}')