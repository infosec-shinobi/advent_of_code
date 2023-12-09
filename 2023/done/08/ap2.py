from math import gcd

def find_lcm(num1, num2):
    gcd_value = gcd(num1, num2)
    lcd = (num1*num2)/gcd_value
    return int(lcd)

directions = []
map_of_cord = {}
current_location = []
count = 1

#with open('ep2.txt') as f:
with open('i.txt') as f:

    for line in f:
        line = line.strip()
        if count == 1:
            directions = line
        elif count == 2:
            pass
        else:
            cord, values = line.split(" = (")
            left, right = values.split(", ")
            right, _ = right.split(")")
            map_of_cord[cord] = [left,right]
            if cord[2] == "A":
                current_location.append(cord)
        count += 1

goal_met = False
direction_place = 0
steps = 0
steps_for_z = []
while not goal_met:
    new_cords = []
    next_dir = directions[direction_place]
    end = True
    steps +=1
    for coordinates in current_location:
        new_dir =""
        if next_dir == "L":
            new_dir =map_of_cord[coordinates][0]
        else:
            new_dir = map_of_cord[coordinates][1]
        if new_dir[2] == "Z":
            steps_for_z.append(steps)
        else:
            new_cords.append(new_dir)
    current_location = new_cords
    if len(current_location) == 0:
        goal_met = True
    if direction_place == len(directions) -1:
        direction_place = 0
    else:
        direction_place +=1

if len(steps_for_z) > 0:
    lcm = int(steps_for_z[0])
    steps_for_z.pop(0)

for step_count in steps_for_z:
    lcm = find_lcm(lcm,int(step_count))

print(f'Part 2: {lcm}')