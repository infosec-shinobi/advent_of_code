# https://adventofcode.com/2020/day/5
# --- Day 5: Binary Boarding ---

def find_seat_cords(binary_str):
    """Translate binary string to seat coordinates"""

    row_low = 0
    row_high = 127
    column_low = 0
    column_high = 7
    current_row_half = 64
    current_column_half = 4
    row = ""
    column = ""

    for letter in binary_str:

        #print(f"row low: {row_low} row high: {row_high}")
        if letter == "F":
            #take lower half
            if row_high - row_low == 1:
                row = row_low
            else:
                row_high = row_high - current_row_half
                current_row_half = int(current_row_half/2)
        elif letter == "B":
            #take upper half
            if row_high - row_low == 1:
                row = row_high
            else:
                row_low = row_high - current_row_half + 1
                current_row_half = int(current_row_half/2)
        if letter == "L":
            #take lower half
            if column_high - column_low == 1:
                column = column_low
            else:
                column_high = column_high - current_column_half
                current_column_half = int(current_column_half/2)
        elif letter == "R":
            #take upper half
            if column_high - column_low == 1:
                column = column_high
            else:
                column_low = column_high - current_column_half + 1
                current_column_half = int(current_column_half/2)
        else:
            continue
    return row, column

def get_seat_id(row_n, column_n):
    """Find seat id given seat coordinates"""
    #Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
    return row_n*8+column_n


def main():
    #open input file
    f = open("input.txt", "r")
    #f = open("test.txt", "r")

    input_list = []
    for x in f:
        input_list.append(x.strip())
  
    #exercise part 1
    
    high_seat_id = 0
    temp_seat_id = 0
    seat_ids = []

    for item in input_list:
        row_num, column_num = find_seat_cords(item)
        temp_seat_id = get_seat_id(row_num, column_num)
        seat_ids.append(int(temp_seat_id))
        if temp_seat_id > high_seat_id:
            high_seat_id = temp_seat_id
        
    print(f"hightest seat id: {high_seat_id}")
    
    # exercise part 2
    #sort list
    seat_ids.sort()
    seat_count = len(seat_ids)
    #cycle thru the list and find where previous + 1 doesn't equal current
    for number in range(1,seat_count-1,1):
        previous_n = seat_ids[number-1]
        cur_n = seat_ids[number]
        if previous_n + 1 != cur_n:
            print(f"My seat id is: {cur_n-1}") 
        else:
            continue

if __name__ == "__main__":
    main()