import math

def main():
    #open input file
    f = open("input.txt", "r")
    #f = open("ex_input.txt", "r")

    input_list = []

    #read each line and add to list
    for line in f:
        input_list = line.split(",")
    
    for i in range(0,len(input_list), 4):
        action = input_list[i]
        if action == "99":
            return
        p1 = input_list[i+1]
        p2 = input_list[i+2]
        final = input_list[i+3]

        print(f"{action}, {p1}, {p2}, {final}")
        
        p1v = input_list[int(p1)]   
        p2v = input_list[int(p2)]
        if action == "1":
            temp = int(p1v)+int(p2v)
            input_list[int(final)] = temp
        elif action == "2":
            temp = int(p1v)*int(p2v)
            input_list[int(final)] = temp
        else:
            return

    print(f"Part oew: {input_list[0]}")
if __name__ == "__main__":
    main()
