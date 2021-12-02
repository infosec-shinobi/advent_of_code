values = []
#with open('example.txt') as f:
with open('input.txt') as f:
    for line in f:
        values.append(line)

##########
# Part 1 #
##########

horizontal_p =0
depth_p = 0

for item in values:
    data = item.split(" ", 2)

    if data[0] == "up":
        depth_p-=int(data[1])
    elif data[0] == "down":
        depth_p+=int(data[1])
    else:
        horizontal_p+=int(data[1])

print(f'Part 1\nh: {horizontal_p} d: {depth_p}\nProduct: {horizontal_p*depth_p}')

##########
# Part 2 #
##########

horizontal_p =0
depth_p = 0
aim = 0

for item in values:
    data = item.split(" ", 2)

    if data[0] == "up":
        aim-=int(data[1])
    elif data[0] == "down":
        aim+=int(data[1])
    else:
        horizontal_p+=int(data[1])
        depth_p+=aim*int(data[1])


print(f'Part 2\nh: {horizontal_p} d: {depth_p} a: {aim}\nProduct: {horizontal_p*depth_p}')