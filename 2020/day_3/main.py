# https://adventofcode.com/2020/day/3
# Day 3: Toboggan Trajectory

from math import ceil, prod

def hit_or_miss(mountain, slope):
    """Determines how many trees are hit on a mountain when provided a slope"""
    #Trackers
    hit_count = 0
    y_slope = slope[1]
    x_slope = slope[0]
    x_cur = 0
    
    #move according to the slope provided, assuming the first slope on the first round
    for y in range(y_slope, len(mountain), y_slope):
        x_cur += x_slope
        current_pos = mountain[y][x_cur]
        if current_pos == "#":
            hit_count += 1
    return hit_count

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        input_list.append(x.strip())

    #exercise part 1
    #determine how many times to repeat pattern
    max_slope = 7
    num_of_rows = len(input_list)
    num_of_columns = len(input_list[0])
    req_columns = max_slope*num_of_rows

    #determine how many times pattern should repeat
    #don't forget to round up
    duplicate_req = ceil(req_columns/num_of_columns)
 
    #update list for full pattern
    for index_num in range(len(input_list)):
        temp_list = []
        add_string = (str(input_list[index_num])*duplicate_req)
        temp_list.extend(add_string)
        input_list[index_num] = temp_list

    #exercise part 2
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    trees_hit = []

    for row in slopes:
        hits = hit_or_miss(input_list,row)
        trees_hit.append(hits)
        print(f"For slope {row}, trees hit: {hits}")

    print(f"Product of all trees hit: {prod(trees_hit)}")

if __name__ == "__main__":
    main()