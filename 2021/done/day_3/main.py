values = []

with open('input.txt') as f:
#with open('ex.txt') as f:
    for line in f:
        line = line.strip()
        values.append(line)

##########
# Part 1 #
##########

power_consumption = 0
gamma_rate =""
epsilon_rate = ""

tracking_list = []

for item in values:
    for num in range(0,len(item)):
        if len(tracking_list) <= num:
            tracking_list.append({})
        temp_dic = tracking_list[num]
        temp_dic[item[num]] = temp_dic.get(item[num], 0) + 1
        tracking_list[num] = temp_dic

for item in tracking_list:
    zero = item["0"]
    one = item["1"]
    if zero > one:
        gamma_rate += "0"
        epsilon_rate +="1"
    else:
        gamma_rate += "1"
        epsilon_rate +="0"
power_consumption = int(gamma_rate,2)*int(epsilon_rate,2)
print(f'Part 1: {power_consumption}')

##########
# Part 2 #
##########

oxygen_list = values
list_pos = 0
solved = False

while not solved:
    temp_0 = []
    temp_1 = []
    if len(oxygen_list) == 1:
        solved = True
    else:
        for item in oxygen_list:
            if item[list_pos] == "0":
                temp_0.append(item)
            else:
                temp_1.append(item)
        list_pos+=1
        if len(temp_0)>len(temp_1):
            oxygen_list = temp_0
        elif len(temp_0)==len(temp_1):
            oxygen_list = temp_1
        else:
            oxygen_list = temp_1

co2_list = values
list_pos = 0
solved = False

while not solved:
    temp_0 = []
    temp_1 = []
    if len(co2_list) == 1:
        solved = True
    else:
        for item in co2_list:
            if item[list_pos] == "0":
                temp_0.append(item)
            else:
                temp_1.append(item)
        list_pos+=1
        if len(temp_0)>len(temp_1):
            co2_list = temp_1
        elif len(temp_0)==len(temp_1):
            co2_list = temp_0
        else:
            co2_list = temp_0
life_support = int(oxygen_list[0],2)*int(co2_list[0],2)
print(f'Part 2: {life_support}')
