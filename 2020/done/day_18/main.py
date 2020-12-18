# https://adventofcode.com/2020/day/18
# --- Day 18: Operation Order ---

# Not happy with the duplicate functions... Need to revisit and clean up at some point

import re

def has_addition(temp_list):
    """replaces addition statements with the value it equates to"""
    more_additions = True
    current_line = temp_list
    #Loop until all additions are gone
    while more_additions:
        #find first addition
        first_addition = current_line.index('+')
        #determine what that expression equals
        temp_placeholder = evaluate_exp(current_line[first_addition-1:first_addition+2])
        #form a new current line
        new_line = current_line[0:first_addition-1]
        new_line.append(str(temp_placeholder))
        #check for line ending in param to avoid index error
        if len(current_line) - first_addition+1 != 0:
            new_line.extend(current_line[first_addition+2:])
        current_line = new_line

        #check if any more addition
        addition_count = current_line.count("+")
        if addition_count == 0:
            more_additions = False
    #evaluate the final line with no addition

    if len(current_line) == 1:
        return int(current_line[0])
    else:
        return evaluate_exp(current_line)

def has_paranths(temp_list):
    """replaces paranths statements with the value it equates to"""
    more_paranths = True
    current_line = temp_list
    #Loop until all paranths are gone
    while more_paranths:
        #find last first paranth and the corresponding closing paranth
        last_first_paranth = len(current_line)-1-current_line[::-1].index('(')
        corresponding_close_paranth = current_line[last_first_paranth:].index(')')+last_first_paranth
        #determin what that expression in the paranths equals
        temp_placeholder = evaluate_exp(current_line[last_first_paranth+1:corresponding_close_paranth])

        #form a new current line
        new_line = current_line[0:last_first_paranth]
        new_line.append(str(temp_placeholder))
        #check for line ending in param to avoid index error
        if corresponding_close_paranth < len(temp_list):
            new_line.extend(current_line[corresponding_close_paranth+1:])
        current_line = new_line
        #check if any more paranths
        paranth_count = current_line.count("(")
        if paranth_count == 0:
            more_paranths = False
    #evaluate the final line with no paranths
    temp_placeholder = evaluate_exp(current_line)
    return temp_placeholder

def has_paranthspt2(temp_list):
    """replaces paranths statements with the value it equates to"""
    more_paranths = True
    current_line = temp_list
    #Loop until all paranths are gone
    while more_paranths:
        #find last first paranth and the corresponding closing paranth
        last_first_paranth = len(current_line)-1-current_line[::-1].index('(')
        corresponding_close_paranth = current_line[last_first_paranth:].index(')')+last_first_paranth
        #determin what that expression in the paranths equals
        temp_placeholder = evaluate_exp2(current_line[last_first_paranth+1:corresponding_close_paranth])

        #form a new current line
        new_line = current_line[0:last_first_paranth]
        new_line.append(str(temp_placeholder))
        #check for line ending in param to avoid index error
        if corresponding_close_paranth < len(temp_list):
            new_line.extend(current_line[corresponding_close_paranth+1:])
        current_line = new_line
        #check if any more paranths
        paranth_count = current_line.count("(")
        if paranth_count == 0:
            more_paranths = False
    #evaluate the final line with no paranths
    temp_placeholder = evaluate_exp2(current_line)
    return temp_placeholder

def evaluate_exp(math_problem):
    """function to determine the answer to the math problem"""

    total = 0
    paranths = math_problem.count("(")

    if paranths == 0:
        total = int(math_problem[0])
        temp_value = has_addition
        for index, item in enumerate(math_problem):
            if item == "+":
                total = total+int(math_problem[index+1])
            elif item == "*":
                total = total*int(math_problem[index+1])
    else:
        total = has_paranths(math_problem)
    return total

def evaluate_exp2(math_problem):
    """function to determine the answer to the math problem for part 2"""

    total = 0
    paranths = math_problem.count("(")
    addition = math_problem.count("+")
    if paranths == 0:
        if addition == 0:
            total = int(math_problem[0])
            for index, item in enumerate(math_problem):
                if item == "*":
                    total = total*int(math_problem[index+1])
        else:
            total = has_addition(math_problem)
        return total
    else:
        total = has_paranthspt2(math_problem)
    return total

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        input_list.append(x.strip())

    overall_sum_pt1 = 0
    overall_sum_pt2 = 0
    for item in input_list:
        #print("="*80)
        temp_line = []
        temp_list = re.split('([+*()])', item)
        for thing in temp_list:
            temp_line.append(thing.strip())
        temp_line = list(filter(None, temp_line))
        pt1_total = evaluate_exp(temp_line)
        #print(f"P1 temp total is: {pt1_total}")
        overall_sum_pt1 += pt1_total
        pt2_total = evaluate_exp2(temp_line)
        #print(f"P2 temp total is: {pt2_total}")
        overall_sum_pt2 += pt2_total
    
    print(f"Pt1 sum {overall_sum_pt1}\nPt2 sum {overall_sum_pt2}")

if __name__ == "__main__":
    main()