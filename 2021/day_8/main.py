signals_per_num = {
    0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6
 }


display = []
output = {}

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        temp_list = line.strip().split("|")
        print(temp_list)
        display.append(temp_list[0].split())
        temp_output = temp_list[1].split()

        for item in temp_output:
            if item in output:
                output[item]+=1
            else:
                output[item]= 1

##########
# Part 1 #
##########

#how many times do digits 1, 4, 7, or 8 appear
# len of 2, 4, 3, 7

total = 0

for key, value in output.items():
    if len(key) in [2,4,3,7]:
        total += value
print(f'Part 1: {total}')

##########
# Part 2 #
##########
"""
    1: cf      2
    7: acf     3
    4: bcdf    4
    2: acdeg   5
    3: acdfg   5
    5: abdfg   5
    0: abcefg  6
    6: abdefg  6
    9: abcdfg  6
    8: abcdefg 7

We know 
"""
lookup_map = {'a':'','b':'','c':'','d':'','e':'','f':'','g':''}
numb_map = {'1':'cf','7': 'acf','4': 'bcdf', '2': 'acdeg','3': 'acdfg',
    '5': 'abdfg', '0': 'abcefg','6': 'abdefg','9': 'abcdfg','8': 'abcdefg'}

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

 """
 if we have item length 2 we know [cf]
 if we have item length 3 we know [a] if we already know [cf]
 if we have item length of 4 we know [bd] if we know [cf]
 if we have item length of 5 and we know [cf], we can figure out 2 (doesn't have [cf]), which will give us [eg] < should be able to determine e from this...


 """

#print(f'Part 2: {increase_win}')