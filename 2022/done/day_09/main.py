values = []
tracker = {"0,0":{"h":True, "0":True, "1":True, "2":True, "3":True, "4":True, "5":True, "6":True, "7":True, "8":True}}
h_lat, h_long = 0, 0
knot_tracker = ["0,0","0,0","0,0","0,0","0,0","0,0","0,0","0,0","0,0"]

def tail_movement(f_long, b_long, f_lat, b_lat):
    if f_lat == b_lat:
        if f_long - b_long == 2:
            b_long += 1
        elif f_long - b_long == -2:
            b_long -= 1
        else:
            pass
        b_key = str(b_long) +","+ str(b_lat)
    elif f_long == b_long:
        if f_lat - b_lat == 2:
            b_lat += 1
        elif f_lat - b_lat == -2:
            b_lat -= 1
        else:
            pass
        b_key = str(b_long) +","+ str(b_lat)
    elif abs(f_lat - b_lat) == 2 and abs(f_long - b_long) == 2:
        b_key = str(min(f_long,b_long)+1) +","+str(min(f_lat,b_lat)+1) 
    elif abs(f_lat - b_lat) == 2:
        b_key = str(f_long) +","+str(min(f_lat,b_lat)+1) 
    elif abs(f_long - b_long) == 2:
        b_key = str(min(f_long,b_long)+1) +","+str(f_lat)
    else:
        b_key = str(b_long) +","+ str(b_lat)

    return b_key

#with open('ex.txt') as f:
#with open('ex2.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        instructs = line.split(" ")
        values.append(list(instructs))

for step in values:
    direction = step[0]
    count = step[1]
    for x in range(1, int(count)+1):
        if direction == "R":
            h_long += 1
        elif direction == "L":
            h_long -= 1
        elif direction == "U":
            h_lat += 1
        elif direction == "D":
            h_lat -= 1
        else:
            pass

        h_key = str(h_long) +","+ str(h_lat)

        if h_key in tracker:
            tracker[h_key]["h"] = True
        else:
            tracker[h_key] = {"h":True}

        for x in range(0, len(knot_tracker)):
            if x == 0:
                lead_long = h_long
                lead_lat = h_lat
            else:
                lead_long, lead_lat = return_key.split(",")

            cur_spot = knot_tracker[x]
            current_long, current_lat = cur_spot.split(",")
            return_key = tail_movement(int(lead_long), int(current_long), int(lead_lat), int(current_lat))

            if return_key in tracker:
                tracker[return_key][str(x)] = True
            else:
                tracker[return_key]= {str(x): True}

            knot_tracker[x] = return_key

##########
# Part 1 #
##########
total = 0

for k,v in tracker.items():
    if v.get("0", False):
        total +=1
print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0
for k,v in tracker.items():
    if v.get("8", False):
        total_2 +=1
print(f'Part 2: {total_2}')