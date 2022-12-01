steps = 0
actions = {}

#with open('ex.txt') as f:
#with open('ex2.txt') as f:
with open('input.txt') as f:
#on x=10..12,y=10..12,z=10..12
    for line in f:
        steps +=1
        line = line.strip()
        temp_action = line.split(' ')
        action = temp_action[0]
        temp_moves = temp_action[1].split(',')
        x_temp = temp_moves[0]
        y_temp = temp_moves[1]
        z_temp = temp_moves[2]
        x_temp = x_temp.split('=')
        x_temp = x_temp[1].split('..')
        x_temp[0] = int(x_temp[0])
        x_temp[1] = int(x_temp[1])
        y_temp = y_temp.split('=')
        y_temp = y_temp[1].split('..')
        y_temp[0] = int(y_temp[0])
        y_temp[1] = int(y_temp[1])
        z_temp = z_temp.split('=')
        z_temp = z_temp[1].split('..')
        z_temp[0] = int(z_temp[0])
        z_temp[1] = int(z_temp[1])
        actions[steps] = {'action':action, 'x':x_temp, 'y':y_temp, 'z':z_temp}
    
for k,v in actions.items():
    print(k,v)

##########
# Part 1 #
##########
total = 0
p1_tracker = {}

def perform_instruc(step_count, current_dict):
    step_instructions = actions[step_count]
    start_x = min(step_instructions['x'])
    stop_x = max(step_instructions['x'])
    start_y = min(step_instructions['y'])
    stop_y = max(step_instructions['y'])
    start_z = min(step_instructions['z'])
    stop_z = max(step_instructions['z'])
    lights = step_instructions['action']

    if start_x < -50 or start_y < -50 or start_z < -50:
        return current_dict
    if stop_x > 50 or stop_y > 50 or stop_z > 50:
        return current_dict
    
    for x in range(start_x, stop_x+1):
        for y in range(start_y, stop_y+1):
            for z in range(start_z, stop_z+1):
                key = x,y,z
                if lights == "off":
                    current_dict.pop(key, None)
                else:
                    current_dict[key] = "on"
    return current_dict

for step in range(1, steps+1):
    p1_tracker = perform_instruc(step, p1_tracker)

total = len(p1_tracker.keys())
print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0

print(f'Part 2: {total_2}')