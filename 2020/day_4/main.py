# https://adventofcode.com/2020/day/4
# --- Day 4: Passport Processing ---
import re

def str_to_map(cur_string):
    """translate string to map"""
    #parse the lines twice to create the dic
    temp_dic = dict((x.strip(), y.strip()) 
             for x, y in (element.split(':')  
             for element in cur_string.split(" ")))
    
    return temp_dic

def validate_data(data_dic):
    """validate values in dic"""
    #Validate birthyear
    if int(data_dic["byr"]) < 1920 or int(data_dic["byr"]) > 2002:
        return False
    #Validate issue year
    if int(data_dic["iyr"]) < 2010 or int(data_dic["iyr"]) > 2020:
        return False
    #Validate expiration year
    if int(data_dic["eyr"]) < 2020 or int(data_dic["eyr"]) > 2030:
        return False  
    #Validate height
    if re.search("^[0-9]*(cm|in)$", data_dic["hgt"]):
        #get the int from the string
        nums = re.findall(r'\d+',data_dic["hgt"])
        if re.search("(cm)$", data_dic["hgt"]):
            if int(nums[0]) < 150 or int(nums[0]) > 193:
                return False
        else:
            if int(nums[0]) < 59 or int(nums[0]) > 76:
                return False
    else: 
        return False
   #Validate hair color
    if re.search("^[#][0-9,a-f]{6}$", data_dic["hcl"]):
        pass
    else:
        return False
   #Validate eye color
    if re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", data_dic["ecl"]):
        pass
    else:
        return False
    #Validate passport id
    if re.search("^[0-9]{9}$", data_dic["pid"]):
        pass
    else:
        return False

    #If all checks pass, return True
    return True

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []
    temp_line = ""
    #read each line, preprocess, and add to list
    for x in f:
        if x == "\n":
            input_list.append(temp_line)
            temp_line = ""
        else:
            if temp_line == "":
                temp_line = x.strip()
            else:
                temp_line = temp_line + " " + x.strip()
    #Gotta add the last passport that doesn't have a newline after it
    input_list.append(temp_line)

    #exercise part 1
    req_passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passport = 0

    for item in input_list:
        cur_dic = str_to_map(str(item))
        valid = True
        #check for required keys in passport
        for field in req_passport_fields:
            if field in cur_dic: 
                pass
            else: 
                valid = False
        # exercise part 2
        if valid:
            valid = validate_data(cur_dic)

        if valid:
            valid_passport += 1

    print(f"# of valid passports: {valid_passport}")

if __name__ == "__main__":
    main()