# https://adventofcode.com/2020/day/1
# Day 1: Report Repair
from itertools import combinations 

def product(tup):
    """Calculates the product of a tuple"""
    prod = 1
    for x in tup:
        prod = prod * x
    return prod

def sum_finder(tup_list, desired_sum):
    """Takes a list of tuples and attempts to find the tuple that sums to a desired number"""
    for item in tup_list:
        if sum(list(item)) == desired_sum:
            print(f"Sum of {item} is 2020. Product is {product(item)}")
            return
    print(f"{desired_sum} not found!")

def main():
    #open input file
    f = open("input.txt", "r")

    temp_list = []
    #read each line and add to list
    for x in f:
        temp_list.append(int(x))

    #convert to dict to remove dups (if any) and convert back to list
    temp_list = list(dict.fromkeys(temp_list))

    #exercise part 1
    combos = list(combinations(temp_list,2))
    sum_finder(combos, 2020)
    
    #exercise part 2
    combos = list(combinations(temp_list,3))
    sum_finder(combos, 2020)

if __name__ == "__main__":
    main()