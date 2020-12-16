# https://adventofcode.com/2020/day/12
# --- Day 12: Rain Risk ---

def get_key(cur_dict, search_item):
    """get key from value in a dictionary"""
    for key, value in cur_dict.items():
         if search_item == value:
             return key
    return "key doesn't exist"

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        input_list.append(x.strip())

    #print(input_list)

    direction_dict = {"north":0, "south":0, "east":0, "west":0}
    coordinates = {0:"east", 1:"south", 2:"west", 3:"north"}
    current_dir = 0
    
    for item in input_list:
        direction = item[0]
        moves = int(item[1:])
        print(f"================\n{direction_dict}\n")
        print(f"Current dir: {current_dir}, dir to move {direction}, num of moves {moves}")
        
        if direction == "N":
            direction_dict["north"] = direction_dict.get('north', 0) + moves
        elif direction == "S":
            direction_dict["south"] = direction_dict.get('south', 0) + moves
        elif direction == "E":
            direction_dict["east"] = direction_dict.get('east', 0) + moves
        elif direction == "W":
            direction_dict["west"] = direction_dict.get('west', 0) + moves
        elif direction == "F":
            print(f"Current dir to move fwd: {current_dir}")
            current_dir_name = coordinates[current_dir]
            print(f"Current dir to move fwd: {current_dir}, current dir name: {current_dir_name}")
            print(f"Moving from {direction_dict[current_dir_name]} to {direction_dict[current_dir_name]+moves}")
            direction_dict[current_dir_name] = direction_dict.get(current_dir_name, 0) + moves
        elif direction == "R":
            if (moves/90) + current_dir >= 4:
                current_dir = int((moves/90) - (4 - current_dir))
            else:
                current_dir = int((moves/90) + current_dir)
            print(f"New dir: {current_dir}")
        elif direction == "L":
            if current_dir - (moves/90) < 0:
                current_dir = int(4 - ((moves/90) - current_dir))

                4 - (1-0)
            else:
                current_dir = int(current_dir-(moves/90))
            print(f"New dir: {current_dir}")
 
    print(direction_dict)
    manhattan = abs(direction_dict["east"]- direction_dict["west"])+abs(direction_dict["north"] - direction_dict["south"])
  
    print(manhattan)
  
if __name__ == "__main__":
    main()