def check_cycle(cycle_num, x_value):
    if cycle_num in desired_cycle_list:
        desired_cycles[cycle_num] = x_value
    return (cycle+1)

def check_sprite(x_value, crt_l, crt_r):
    spritel = x_value-1
    spritem = x_value
    spriter = x_value+1

    if crt_l == spritel or crt_l == spritem or crt_l == spriter:
        crt[crt_r][crt_l] = str("#")
    else:
        pass

    if crt_l == 39 and crt_r <5:
        crt_l = 0
        crt_r += 1
    else:
        crt_l += 1

    return crt_l, crt_r


values = []

#with open('ex.txt') as f:
#with open('ex2.txt') as f:
with open('input.txt') as f:
    for line in f:
        temp_list = []
        line = line.strip().split(" ")
        values.append(line)

x = 1
cycle = 1
desired_cycles = {20:0, 60:0, 100:0, 140:0, 180:0, 220:0}
desired_cycle_list = list(desired_cycles.keys())
initial_crt_list = ["."]*40
crt = []
crt_row = 0
crt_loc = 0

for rows in range(1, 7):
    crt.append(initial_crt_list.copy())

for item in values:
    if item[0] == "noop":
        cycle = check_cycle(cycle, x)
        crt_loc, crt_row = check_sprite(x, crt_loc, crt_row)
    else:
        x_change = item[1]
        for waiting in range(1,3):
            cycle = check_cycle(cycle, x)
            crt_loc, crt_row = check_sprite(x, crt_loc, crt_row)
        x += int(x_change)

##########
# Part 1 #
##########
total = 0 #signal strength

for k,v in desired_cycles.items():
    total += int(k)*int(v)
print(f'Part 1: {total}')

##########
# Part 2 #
##########

print(f'Part 2:')

for line in crt:
    print("".join(line))