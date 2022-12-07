directories = {"/":{"parent_dir": "n/a", "contents":[]}}
files = {}
current_dir = "/"
parent_dir = "/"
temp_list = []

def dir_size(pwd, list_of_items):
    total_size = 0
    for item in list_of_items:
        if item[0] == "/":
            total_size += dir_size(item, directories[item]["contents"])
        else:
            total_size += files[item][pwd]
    return total_size

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        output = line.split(" ")
        if output[0] == "$":
            if output[1] == "ls":
                pass
            elif output[1] == "cd":
                if output[2] == "/":
                    pass
                elif output[2] == "..":
                    if len(temp_list) != 0:
                        directories[current_dir]["contents"] = temp_list
                        temp_list = []
                    else:
                        pass
                    current_dir = directories[current_dir]["parent_dir"]
                    parent_dir = directories[parent_dir]["parent_dir"]
                else:
                    if len(directories[current_dir]["contents"]) ==0:
                         directories[current_dir]["contents"] = temp_list
                    else:
                        pass
                    temp_list = []
                    parent_dir = current_dir
                    if current_dir == "/":
                        current_dir = current_dir + str(output[2])
                    else:
                        current_dir = current_dir + "/" + str(output[2])
                    directories[current_dir] = {"parent_dir": parent_dir, "contents":[]}
        else:
            if output[0] == "dir":
                if current_dir == "/":
                    temp_list.append(current_dir+str(output[1]))
                else:
                    temp_list.append(current_dir+"/" +str(output[1]))
            else:
                temp_list.append(output[1])
                if output[1] in files.keys():
                    temp_dic = files[output[1]].copy()
                    temp_dic[current_dir] = int(output[0])
                    files[output[1]] = temp_dic
                else:
                    files[output[1]] = {current_dir:int(output[0])}

#account for last folder
directories[current_dir]["contents"] = temp_list

##########
# Part 1 #
##########
total = 0
file_size_tracker = {}

for folder in directories:
    temp_total = dir_size(folder, directories[folder]["contents"])
    file_size_tracker[folder] = temp_total

for size in file_size_tracker.values():
    if size <= 100000:
        total += size
    else:
        pass

print(f'Part 1: {total}')

##########
# Part 2 #
##########

filesystem = 70000000
req_free_space = 30000000
current_free_space = filesystem - file_size_tracker["/"]
delete_size = 0

for value in file_size_tracker.values():
    if (current_free_space + value) > req_free_space:
        if delete_size == 0:
            delete_size = value
        else:
            if value < delete_size:
                delete_size = value
print(f'Part 2: {delete_size}')