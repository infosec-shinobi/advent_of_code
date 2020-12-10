# https://adventofcode.com/2020/day/6
# --- Day 6: Custom Customs ---

def input_to_map(answer_str, user_count):
    """Takes a string, makes it a map, and finds a specific value in the map"""

    # exercise part 2
    temp_dic = {} 
    all_yes = 0
    
    #translate str to map
    for letter in answer_str: 
        temp_dic[letter] = temp_dic.get(letter, 0) + 1
    
    #find value in map
    for answer, count in temp_dic.items():
        if count == user_count:
            all_yes += 1
    
    return all_yes

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []
    temp_line = ""
    all_yes_answers = 0
    users = 0

    #read each line, preprocess, and add to list
    for x in f:
        if x == "\n":
            all_yes_answers = all_yes_answers + input_to_map(temp_line, users)
            input_list.append(temp_line)
            temp_line = ""
            users = 0
        else:
            if temp_line == "":
                users += 1
                temp_line = x.strip()
            else:
                temp_line = temp_line + x.strip()
                users += 1

    #Need to process the last item that doesn't have a newline after it
    input_list.append(temp_line)
    all_yes_answers = all_yes_answers + input_to_map(temp_line, users)

    # exercise part 1
    total_count = 0
    for item in input_list:
        item = list(set(item))
        total_count += len(item)
    
    print(f"Total uniq yes answers: {total_count}\nTotal yes by all only: {all_yes_answers}")  

if __name__ == "__main__":
    main()