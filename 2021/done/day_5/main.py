import copy

values = []

def moves(num1, num2):
    temp_list = []
    for x in range(min(int(num1),int(num2)) ,max(int(num1),int(num2))+1):
        temp_list.append(str(x))
    return temp_list  

def moves_d(x1,y1,x2,y2):
    temp_list = []
    x_add = False
    if x1<x2:
        x_add = True
    y_add = False
    if y1<y2:
        y_add = True

    temp_x = x1
    temp_y = y1
    temp_list.append(f"{x1},{y1}")
    for x in range(abs(int(x1)-int(x2))):
        if x_add:
            temp_x += 1
        else:
            temp_x -= 1
        if y_add:
            temp_y += 1
        else:
            temp_y -= 1
        temp_list.append(f"{temp_x},{temp_y}")
    return temp_list 

def update_dic(add_key, mast_dict):
    if add_key in mast_dict:
        mast_dict[add_key]+=1
    else:
        mast_dict[add_key]=1

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        temp_list = []
        line = line.strip().split(" ")
        p1 = line[0].split(',')
        p2 = line[2].split(',')
        temp_list.append(p1)
        temp_list.append(p2)
        values.append(temp_list)

values2 = copy.deepcopy(values)
##########
# Part 1 #
##########

total = 0
pos_track = {}

for line in values:
    x1=int(line[0][0])
    y1=int(line[0][1])
    x2=int(line[1][0])
    y2=int(line[1][1])
    if x1==x2:
        temp_moves = moves(y1, y2)
        for item in temp_moves:
            new_key = f'{x1},{item}'
            update_dic(new_key, pos_track)
    elif y1==y2:
        temp_moves = moves(x1, x2)
        for item in temp_moves:
            new_key = f'{item},{y1}'
            update_dic(new_key, pos_track)
    else:
        continue

for key, value in pos_track.items():
    if value >= 2:
        total +=1

print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0

pos_track2 = {}

for line in values:
    x1=int(line[0][0])
    y1=int(line[0][1])
    x2=int(line[1][0])
    y2=int(line[1][1])
    if x1==x2:
        temp_moves = moves(y1, y2)
        for item in temp_moves:
            new_key = f'{x1},{item}'
            update_dic(new_key, pos_track2)
    elif y1==y2:
        temp_moves = moves(x1, x2)
        for item in temp_moves:
            new_key = f'{item},{y1}'
            update_dic(new_key, pos_track2) 
    else:
        temp_moves = moves_d(x1,y1,x2,y2)
        for item in temp_moves:
            update_dic(item, pos_track2) 

for key, value in pos_track2.items():
    if value >= 2:
        total_2 +=1

print(f'Part 2: {total_2}')