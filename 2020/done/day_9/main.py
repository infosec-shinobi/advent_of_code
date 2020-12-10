# https://adventofcode.com/2020/day/9
# --- Day 9: Encoding Error ---

from itertools import combinations 
  
def find_pairs(lst_of_nums, sum_value, nums_to_add): 
    """Take in a list of numbers, find all n groupings of numbers in list that sum to a num"""
    return [group for group in combinations(lst_of_nums, nums_to_add) if sum(group) == sum_value] 

def find_contiguous(all_nums, vuln_num): 
    """Take in a list of numbers, find contiguous numbers in list that sum to a num"""

    starting_num = 0
    nums_found = False

    while not nums_found:
        count = 0
        temp_value = 0
        #Make sure we don't go out of index
        if starting_num > len(all_nums):
            print("no matches found.")
            break
        else:
            temp_list = all_nums[starting_num:]

            #iterate over temp list to see if contiguous nums sum to desired value
            for item in temp_list:
                temp_value += item
                count += 1

                if temp_value < vuln_num:
                    pass
                elif temp_value == vuln_num:
                    #return list of contiguous nums
                    return all_nums[starting_num:(starting_num+count)]
                else:
                    starting_num += 1
                    break

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        input_list.append(int(x.strip()))

    weakness_found = False
    starting_num = 0
    current_test_index = 25

    #exercise part 1
    while not weakness_found:
        ending_num = starting_num + 25 #Slice notation stops one short of ending num
        sum_to_find = int(input_list[current_test_index])
        current_preamble = input_list[starting_num:ending_num]
        sums_that_work = find_pairs(current_preamble, sum_to_find, 2)

        if len(sums_that_work) < 1:
            print(f"vuln num: {sum_to_find}")
            vuln_num = sum_to_find
            weakness_found = True
        else:
            starting_num += 1
            current_test_index += 1

    #exercise part 2
    contiguous_nums = find_contiguous(input_list, vuln_num)
    print(f"contiguous list: {contiguous_nums}")
    print(f"Sum of min and max of contiguous list: {min(contiguous_nums)+max(contiguous_nums)}")

if __name__ == "__main__":
    main()