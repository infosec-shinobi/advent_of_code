values = []

#with open('ex.txt') as f:
with open('input.txt') as f:

    for line in f:
        line = line.strip().split(" ")
        values.append(line)

##########
# Part 1 #
##########
total = 0
answer_dict = { "w":0, "x":0, "y":0, "z":0}
letters = ["w","x","y","z"]
start_model_num = 92222222222222
done = False
"""
inp a - Read an input value and write it to variable a.
add a b - Add the value of a to the value of b, then store the result in variable a.
mul a b - Multiply the value of a by the value of b, then store the result in variable a.
div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
attempting to execute div with b=0 or attempting to execute mod with a<0 or b<=0 will cause the program to crash and might even damage the ALU
"""

while not done:
    answer_dict = { "w":0, "x":0, "y":0, "z":0}
    string_num = str(start_model_num)
    input_count =  0
    if "0" not in string_num:
        print(string_num)
        for instruction in values:
            instruct = instruction[0]
            if instruct == "inp":
                answer_dict[instruction[1]] = int(string_num[input_count])
                input_count +=1
            else:
                if instruction[2] in letters:
                    temp_value = int(answer_dict[instruction[2]])
                else:
                    temp_value = int(instruction[2])
                
                if instruct == "add":
                    answer_dict[instruction[1]] += temp_value
                elif instruct == "mul":
                    temp_prod = answer_dict[instruction[1]] * temp_value
                    answer_dict[instruction[1]] = temp_prod
                elif instruct == "div":
                    if temp_value != 0:
                        temp_div = answer_dict[instruction[1]]//temp_value
                        answer_dict[instruction[1]] = temp_div
                elif instruct == "mod":
                    if answer_dict[instruction[1]]<0 or temp_value<=0:
                        pass
                    else: 
                        temp_mod = answer_dict[instruction[1]]%temp_value
                        answer_dict[instruction[1]] = temp_mod
                elif instruct == "eql":
                    if answer_dict[instruction[1]]==temp_value:
                        answer_dict[instruction[1]] = 1
                    else:
                        answer_dict[instruction[1]] = 0
        if answer_dict["z"] == 0:
            done = True
        else:
            print(answer_dict["z"])
            start_model_num -= 1
    else:
        start_model_num -= 1

print(f'Part 1: {start_model_num}')

##########
# Part 2 #
##########

total_2 = 0

print(f'Part 2: {total_2}')