input_list = []
#with open('ep2.txt') as f:
with open('i.txt') as f:
    for line in f:
        _,data = line.split(": ")
        data_list = data.split()
        temp_value = ""
        for item in data_list:
            temp_value += item
        input_list.append(int(temp_value))

time = input_list[0]
distance = input_list[1]

tracker = 0

for millisecond in range(time):
    travel_distance = millisecond*(time-millisecond)
    if travel_distance > distance:
        tracker += 1

print(f'Part 2: {tracker}')