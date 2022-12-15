import ast

def compare_items(l, r):

    if isinstance(l, int):
        if isinstance(r, int):
            return l - r
        else:
            return compare_items([l],r)
    else:
        if isinstance(r, int):
            return compare_items(l,[r])
    
    count = 0
    while count<len(l) and count<len(r):
        result = compare_items(l[count], r[count])
        if result:
            return result
        count +=1

    return len(l) - len(r)

values = []
temp_list = []

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line == "":
            values.append(temp_list)
            temp_list = []
        else:
            line = ast.literal_eval(line)
            temp_list.append(line)
    values.append(temp_list)

##########
# Part 1 #
##########
total = 0
new_list = []

for index, pairs in enumerate(values):
    left = pairs[0]
    right = pairs[1]
    new_list.append(left)
    new_list.append(right)
    result = compare_items(left, right)
    
    if result < 0:
        total += index+1

print(f'Part 1: {total}')

##########
# Part 2 #
##########
total_2 = 0
correct_ord = []

new_list.append([[2]])
new_list.append([[6]])

for index, line in enumerate(new_list):
    if index == 0:
        correct_ord.append(line)
    else:
        result = compare_items(line, correct_ord[-1])
        if result > 0:
            correct_ord.append(line)
        else:
            for index2, item in enumerate(correct_ord):
                result = compare_items(line, item)
        
                if result < 0:
                    correct_ord.insert(index2,line)
                    break

two = correct_ord.index([[2]])
six = correct_ord.index([[6]])

print(f'Part 2: {(two+1)*(six+1)}')