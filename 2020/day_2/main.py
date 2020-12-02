# https://adventofcode.com/2020/day/2
# Day 2: Password Philosophy

def check_password(item):
    """Determine if the password is valid according to old policy"""

    #Parse out important data from the line
    temp_list = item.split()
    policy_range = temp_list[0].split("-")
    letter = temp_list[1].split(":")
    letter = letter[0]
    count = 0

    #Check for occurances of the specified letter
    for x in temp_list[2]:
        if x == letter:
            count += 1
    
    #Check if the letter appears between the min and max allowed
    if count >= int(policy_range[0]) and count <= int(policy_range[1]):
        return 1
    else:
        return 0

def check_password2(item):
    """Determine if the password is valid according to new policy"""

    #Parse out important data from the line
    temp_list = item.split()
    locations = temp_list[0].split("-")
    letter = temp_list[1].split(":")
    letter = str(letter[0])
    location_1 = int(locations[0])-1
    location_2 = int(locations[1])-1
    password = str(temp_list[2])
    count = 0

    #Check for policy compliance
    print(f"{password} {letter} {password[location_1]} {password[location_2]}")
    if password[location_1] == letter:
        count += 1
    if password[location_2] == letter:
        count += 1
   
    # validate only 1 match was found
    if count == 1:
       return 1
    else:
        return 0

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        input_list.append(x)

    #check the validity of each password 
    valid_passwords1 = 0
    valid_passwords2 = 0
    for password in input_list:
        #exercise part 1
        decision1 = check_password(password)
        #exercise part 2
        decision2 = check_password2(password)
        valid_passwords1 += decision1
        valid_passwords2 += decision2
  
    print(f"Part 1: {valid_passwords1} passwords are valid.")
    print(f"Part 2: {valid_passwords2} passwords are valid.")
    
if __name__ == "__main__":
    main()