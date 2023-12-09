from collections import Counter

def find_next_value(history):
    tracker = [history]
    cur_row = history
    all_zeros = False

    while not all_zeros:
        next_row = []
        for pos, number in enumerate(cur_row):
            if pos == 0:
                continue
            next_row.append(number - cur_row[pos-1])
             
        num_freq = Counter(next_row)
        if len(num_freq.keys()) == 1 and 0 in num_freq.keys():
            all_zeros = True
        tracker.insert(0,next_row)
        cur_row = next_row
    
    running_total = 0
    last_value = 0
    new_value = 0
    for pos, history_list in enumerate(tracker):
        if pos == 0:
            continue
        cur_value = history_list[0]
        new_value = cur_value -last_value
        last_value = new_value

    running_total += new_value
    return running_total

input_list = []
#with open('ep1.txt') as f:
with open('i.txt') as f:
    for line in f:
        line = line.strip()
        numbers = line.split()
        temp_list = []
        for number in numbers:
            temp_list.append(int(number))
        input_list.append(temp_list)

total = 0

for num_list in input_list:
    total += find_next_value(num_list)

print(f'Part 1: {total}')