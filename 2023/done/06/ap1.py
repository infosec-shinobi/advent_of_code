input_list = []
#with open('ep1.txt') as f:
with open('i.txt') as f:
    for line in f:
        _,data = line.split(": ")
        data_list = data.split()
        input_list.append(data_list)
#time is input_list[0], distance is input_list[1]

tracker = {}
for place, time_period in enumerate(input_list[0]):
    cur_time = int(time_period)
    min_dis = int(input_list[1][place])
    tracker[cur_time] = 0
    for millisecond in range(1,cur_time):
        travel_distance = millisecond*(cur_time-millisecond)
        if travel_distance > min_dis:
            tracker[cur_time] += 1

total = 1
for _,v in tracker.items():
    total = total * v

print(f'Part 1: {total}')