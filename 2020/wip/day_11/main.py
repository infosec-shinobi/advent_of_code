# https://adventofcode.com/2020/day/8
# --- Day 11: Seating System ---

def find_adj_seats(seating_chart):
    """giving a list, determine seating arrangement"""
    last_row = len(seating_chart)
    new_list = []
    change_count = 0
   
    for count, row_status in enumerate(seating_chart):
        # Rules:
        # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        # Otherwise, the seat's state does not change.
        previous_row = []
        next_row = []
        temp_row = []
        if count == 0:
            for x in range(0,len(row_status)):
                previous_row.append(".")
        elif count == last_row-1:
            for x in range(0,len(row_status)):
                next_row.append(".")
        if previous_row == []:
            previous_row = seating_chart[count-1]
        if next_row == []:
            next_row = seating_chart[count+1]
        
        row_length = len(row_status)
        #print(f"\n{previous_row}\n{row_status}\n{next_row}\n")
        for seat_count, seat in enumerate(row_status):
            #print(seat)
            adj_seats = {}
            
            #  [lb]  [back]   [rb]
            # [left]   [c]   [right]
            #  [lf]  [front]  [rf]

            if seat_count == 0:
                adj_seats["left"] = "."
                adj_seats["lf"] = "."
                adj_seats["lb"] = "."
            else:
                adj_seats["left"] = row_status[seat_count-1]
                adj_seats["lf"] = next_row[seat_count-1]
                adj_seats["lb"] = previous_row[seat_count-1]
            if seat_count == row_length-1:
                adj_seats["right"] = "."
                adj_seats["rf"] = "."
                adj_seats["rb"] = "."
            else:
                adj_seats["right"] = row_status[seat_count+1]
                adj_seats["rf"] = next_row[seat_count+1]
                adj_seats["rb"] = previous_row[seat_count+1]
            
            adj_seats["front"] = next_row[seat_count]
            adj_seats["back"] = previous_row[seat_count]
            
            occupied_adj_seats = sum(value == "#" for value in adj_seats.values())
            #print(f"Occupied seats: {occupied_adj_seats}\nSeat map: {adj_seats}")
            if seat == "L" and occupied_adj_seats == 0:
                temp_row.append("#")
                change_count += 1
                #print("L to #")
            elif seat == "#" and occupied_adj_seats >= 4:
                temp_row.append("L")
                change_count += 1
                #print("# to L")
            else:
                temp_row.append(seat)
                #print(f"stayed {seat}")
        #print(temp_row)
        new_list.append(temp_row)
    return change_count, new_list

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        temp_list = []
        x = x.strip()

        for char in x:
            temp_list.append(char)
        
        input_list.append(temp_list)

    changes_made = True
    updated_seating_chart = input_list
    count = 0
    while changes_made:
        print("============================================================")
        seat_updates = 0
        seat_updates, updated_seating_chart = find_adj_seats(updated_seating_chart)
        count += 1

        for x in updated_seating_chart:
            temp_str = ""
            for y in x:
                temp_str = temp_str + y
            print(temp_str)
            
        print(seat_updates)
        if seat_updates == 0:
            print("no more changes")
            changes_made = False
        else:
            print("Changes made.")
 
    occ_count = 0
    for x in updated_seating_chart:
            for y in x:
                if y == "#":
                    occ_count += 1
    print(f"Occupied seats: {occ_count}")
    print("Done!")          



if __name__ == "__main__":
    main()