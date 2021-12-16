import copy

values = []

def plus_one(list_of_lists):

    for row in range(0,len(list_of_lists)):
        for pos in range(0,len(list_of_lists[row])):
            list_of_lists[row][pos]+=1
    
    return

def check_neighbor(data, row_pos, col_pos):
   
    if (row_pos < 0) or (row_pos >= len(data)):
        return False, []
    if (col_pos < 0) or (col_pos >= len(data[row_pos])):
        return False, []
    if data[row_pos][col_pos] == "~":
        return False, []
    return True, [row_pos,col_pos]
            
def check_flashes(data):

    flashes = 0
    flash_detected = False

    for row in range(0,len(data)):
        for pos in range(0,len(data[row])):
            value = data[row][pos]
            #left, right, up, down, left/up d, left/down d, right/up d, right/down d
            neighbors = [[row, pos-1],[row, pos+1],[row+1, pos],[row-1,pos],[row+1, pos-1],[row-1,pos-1],[row-1,pos+1],[row+1,pos+1]]
            if value == "~":
                continue
            if value > 9:
                flashes +=1
                flash_detected = True
                for neighbor in neighbors:
                    status, lookup_up = check_neighbor(data, neighbor[0],neighbor[1])
                    if status:
                        data[lookup_up[0]][lookup_up[1]] += 1
                data[row][pos] = "~"
            
            
    return flash_detected, data, flashes

def flashed_to_zero(data):
    for row in range(0,len(data)):
        for pos in range(0,len(data[row])):
            if data[row][pos] == "~":
                data[row][pos] = 0
    return data

def check_all_zeros(data):
    all_zeros = True
    for row in range(0,len(data)):
        for pos in range(0,len(data[row])):
            if data[row][pos] != 0:
                all_zeros = False
                return all_zeros
    return all_zeros
    
#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        temp_list = []
        line = line.strip()
        for num in line:
            temp_list.append(int(num))
        values.append(temp_list)

values2 = copy.deepcopy(values)

##########
# Part 1 #
##########

total = 0
step_count = 100

for step in range(0,step_count):
    plus_one(values)
    flashes = True
    
    while flashes:
        flashes, values, new_flashes  = check_flashes(values)
        total += new_flashes
    values = flashed_to_zero(values)

print(f'Part 1: {total}')

##########
# Part 2 #
##########

count_objects = (len(values2)*(len(values2[0])))
all_flashes = False
step_count = 1

while not all_flashes:
    if check_all_zeros(values2):
        all_flashes = True
    else:
        plus_one(values2)
        flashes = True
        
        while flashes:
            flashes, values2, flash_count  = check_flashes(values2)
        values2 = flashed_to_zero(values2)
        step_count += 1

print(f'Part 2: {step_count-1}')