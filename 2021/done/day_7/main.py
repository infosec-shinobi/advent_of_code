values = []

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip().split(",")
        for item in line:
            values.append(int(item))

##########
# Part 1 #
##########
total = 0

values.sort()

med_num = values[len(values)//2]

for item in values:
    total += abs(item - med_num)

print(f'Part 1: {total}')

##########
# Part 2 #
##########

#desired_pos = round(sum(values)/len(values))
desired_pos = sum(values)//(len(values))
#need to circle back and understand why rounding down with floor is required intstead of normal round...
#https://www.reddit.com/r/adventofcode/comments/rars4g/2021_day_7_why_do_these_values_work_spoilers/
part_2_total = 0

for item in values:
    moves = abs(item - desired_pos)
    #print(f'{item} {moves}')
    temp_moves = 0
    if moves == 0:
        pass
    else:
        for num in range(1,moves+1):
            part_2_total += num  

print(f'Part 2: {part_2_total}')