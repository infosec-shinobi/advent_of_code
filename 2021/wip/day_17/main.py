values = []

def in_target_area(cur_x, cur_y,tar_x, tar_y):    
    if int(min(tar_x)) <= cur_x <= int(max(tar_x)):
        if int(min(tar_y)) <= cur_y <= int(max(tar_y)):
            return True
    if cur_x > int(max(tar_x)):
        return "finished"
    if cur_y > int(max(tar_y)):
        return "over"
    if cur_x == 0:
        return "finished"
    return False


def moves(cur_x, cur_y):
    #if x>1 -1, x<1 +1, x=0 0
    # y-1
    if cur_x <0:
        cur_x -=1
    elif cur_x > 0:
        cur_x +=1
    else:
        pass
    cur_y -= 1

    return cur_x, cur_y

# target area: x=20..30, y=-10..-5
with open('ex.txt') as f:
#with open('input.txt') as f:
    for line in f:
        line = line.strip().split(", ")
        temp_x = line[0].split("=")
        x_values = temp_x[1].split("..")
        temp_y = line[1].split("=")
        y_values = temp_y[1].split("..")
        print(f'{x_values} {y_values}')

##########
# Part 1 #
##########
total = 0 # highest y position

#if x>1 -1, x<1 +1, x=0 0
# y-1
start_cords  = {}
y_done = False
x_done = False
y = 0
x = 1

while not x_done:
    y = 0
    while not y_done:
        start_pos = (x,y)
        print(start_pos)
        max_y = y
        done = False
        while not done:
            print(x,y)
            result = in_target_area(x,y,x_values, y_values)
            print(result)
            if result:
                start_cords[start_pos] = max_y
                break
            elif result == "over":
                y_done = True
                x_done = True
                break
            elif result == "finished":
                y_done = True
                x_done = True
                break
            else:
                x,y = moves(x,y)
                if y > max_y:
                    max_y = y
        y+=1
    print("pizza")
    x+=1
    y_done = False

print(start_cords)

print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0

print(f'Part 2: {total_2}')