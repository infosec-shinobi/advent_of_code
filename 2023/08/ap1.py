directions = []
map_of_cord = {}
count = 1

#with open('ep1.txt') as f:
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
        count += 1

current_location = "AAA"
goal = "ZZZ"
direction_place = 0
steps = 0
while current_location != goal:
    next_dir = directions[direction_place]
    if next_dir == "L":
        current_location = map_of_cord[current_location][0]
    else:
        current_location = map_of_cord[current_location][1]
    
    if direction_place == len(directions) -1:
        direction_place = 0
    else:
        direction_place +=1
    steps +=1

print(f'Part 1: {steps}')