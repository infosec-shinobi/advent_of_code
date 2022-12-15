values = []
start = (500,0)
y_max = 0
blocked_spots = set()

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        temp_list = []
        line = line.strip()
        new_line = line.split(" -> ")
        for item in new_line:
            temp = item.split(",")
            x, y = temp
            if int(y) > y_max:
                y_max = int(y)
            temp_list.append((int(x),int(y)))
        values.append(temp_list)

for rock_group in values:
    for segments in range(0,len(rock_group)-1):
        line_p1 = rock_group[segments]
        line_p2 = rock_group[segments+1]
        line_x_max = max(line_p1[0],line_p2[0])
        line_x_min = min(line_p1[0],line_p2[0])
        line_y_max = max(line_p1[1],line_p2[1])
        line_y_min = min(line_p1[1],line_p2[1])

        for x in range(line_x_min, line_x_max+1):
            for y in range(line_y_min, line_y_max+1):
                blocked_spots.add((x,y))

##########
# Part 1 #
##########
total = 0
endless_pit = False

while not endless_pit:
    current_x = start[0]
    current_y = start[1]
    while True:
        if current_y > y_max:
            endless_pit = True
            break
        else:
            #can move down
            if (current_x, current_y+1) not in blocked_spots:
                current_y += 1
            #can move left
            elif (current_x-1, current_y+1) not in blocked_spots:
                current_x -= 1
                current_y += 1
            #can move right
            elif (current_x+1, current_y+1) not in blocked_spots:
                current_x += 1
                current_y += 1
            else:
                blocked_spots.add((current_x, current_y))
                total +=1
                break

print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = total
infinity_floor = y_max + 2

hole_blocked = False

while not hole_blocked:
    current_x = start[0]
    current_y = start[1]
    while True:
        if current_y+1 == infinity_floor:
            blocked_spots.add((current_x, current_y))
            total_2 +=1
            break
        #can move down
        elif (current_x, current_y+1) not in blocked_spots:
            #print("down")
            current_y += 1
        #can move left
        elif (current_x-1, current_y+1) not in blocked_spots:
            current_x -= 1
            current_y += 1
        #can move right
        elif (current_x+1, current_y+1) not in blocked_spots:
            current_x += 1
            current_y += 1
        elif (current_x, current_y) == start:
            total_2 += 1
            hole_blocked = True
            break
        else:
            blocked_spots.add((current_x, current_y))
            total_2 +=1
            break

print(f'Part 2: {total_2}')