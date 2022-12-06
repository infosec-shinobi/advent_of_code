values = []

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        values.append(line.strip())

##########
# Part 1 #
##########
total = []

for code in values:
    tracker = []
    count = 0
    uniq = False
    for letter in code:
        if len(tracker) != 4:
            tracker.append(letter)
            count += 1
        else:
            for x in tracker:
                letter_count = tracker.count(x)
                if letter_count != 1:
                    uniq = False
                    break
                else:
                    uniq = True
            if uniq:
                total.append(count)
                break
            else:
                count += 1
                tracker.pop(0)
                tracker.append(letter)

print(f'Part 1: {total}')


##########
# Part 2 #
##########

total_2 = []

for code in values:
    tracker = []
    count = 0
    uniq = False
    for letter in code:
        if len(tracker) != 14:
            tracker.append(letter)
            count += 1
        else:
            for x in tracker:
                letter_count = tracker.count(x)
                if letter_count != 1:
                    uniq = False
                    break
                else:
                    uniq = True
            if uniq:
                total_2.append(count)
                break
            else:
                count += 1
                tracker.pop(0)
                tracker.append(letter)

print(f'Part 2: {total_2}')