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

    print(input_list)

    direction_dict = {"north":0, "south":0, "east":0, "west":0}
    coordinates = {"north":0, "south":180, "east":90, "west":270}
    current_dir = "east"
    
    for item in input_list:
        direction = item[0]
        moves = int(item[1:])
        print(direction, moves)
        print(direction_dict)
        print(current_dir)
        if direction == "N":
            direction_dict["north"] = direction_dict.get('north', 0) + moves
        elif direction == "S":
            direction_dict["south"] = direction_dict.get('south', 0) + moves
        elif direction == "E":
            direction_dict["east"] = direction_dict.get('east', 0) + moves
        elif direction == "W":
            direction_dict["west"] = direction_dict.get('west', 0) + moves
        elif direction == "F":
            print(current_dir)
            direction_dict[current_dir] = direction_dict.get(current_dir, 0) + moves
        elif direction == "R":
            current_dir_value = int(coordinates[current_dir])
            new_value = current_dir_value + moves
            print(new_value)
            if new_value >= 360:
                new_value = new_value-360
                print("FOUND IT")
                print(new_value)
            new_dir_value = get_key(coordinates, new_value)
            current_dir = new_dir_value
        elif direction == "L":
            if current_dir == "north":
                if moves == 90:
                    current_dir ="west"
                elif moves == 180:
                    current_dir = "south"
                elif moves == 270:
                    current_dir = "east"
            if current_dir == "east":
                if moves == 90:
                   current_dir ="north"
                elif moves == 180:
                    current_dir = "west"
                elif moves == 270:
                    current_dir = "south"
            if current_dir == "south":
                if moves == 90:
                   current_dir ="east"
                elif moves == 180:
                    current_dir = "north"
                elif moves == 270:
                    current_dir = "west"
            if current_dir == "west":
                if moves == 90:
                   current_dir ="south"
                elif moves == 180:
                    current_dir = "east"
                elif moves == 270:
                    current_dir = "north"
 
    print(direction_dict)
    manhattan = abs(direction_dict["east"]- direction_dict["west"])+abs(direction_dict["north"] - direction_dict["south"])
  
    print(manhattan)
  
if __name__ == "__main__":
    main()