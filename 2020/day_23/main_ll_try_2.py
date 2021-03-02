# https://adventofcode.com/2020/day/23
# --- Day 23: Crab Cups ---

#Linked List Python Resource: https://stackabuse.com/python-linked-lists/

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
    
    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False

    def print_value(self):
        return self.data, self.next

class SingleLinkedList:
    def __init__(self):
        "constructor to initiate this object"
        
        self.head = None
        self.tail = None
        return
    
    def add_list_item(self, item):
        "add an item at the end of the list"
        print(item)
        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
            
        return
    
    def list_length(self):
        "returns the number of list items"
        
        count = 0
        current_node = self.head
        
        while current_node is not None:
            # increase counter by one
            count = count + 1
            
            # jump to the linked node
            current_node = current_node.next
            
        return count
    
    def output_list(self):
        "outputs the list (the value of the node, actually)"
        
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            print(current_node.next)
            
            # jump to the linked node
            current_node = current_node.next
            
        return
    
    def unordered_search (self, value):
        "search the linked list for the node that has this value"
        
        # define current_node
        current_node = self.head
        
        # define position
        node_id = 1
        
        #node_value = 0
        next_node_value = 0 
        
        while current_node is not None:
            if current_node.has_value(value):
                #node_value = node_id
                next_node_value = current_node.next
                break
                
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        print(f"Next node: {next_node_value}")
        return next_node_value  

    def update_node (self, value, new_next):
        "update node"
        
        # define current_node
        current_node = self.head
        
        # define position
        node_id = 1
        
        #node_value = 0
        next_node_value = 0 
        
        while current_node is not None:
            print(f"current node: {current_node}")
            print(f"Node looks like: {current_node.print_value()}")
            if current_node.has_value(value):
                #node_value = node_id
                current_node.next = new_next
                break
                
            # jump to the linked node
            current_node = current_node.next
            print(f"New current node: {current_node}")
            node_id = node_id + 1
        
        return    

def shuffle_cups(cup_order, move_count, max_len, cur_cup, cur_cup_idx):
    """crab shuffles the cups"""

    #cup_dict = {}
    #prev_node = None
    #first_node = None
    
    cup_list = SingleLinkedList()
    print("cup list length: %i" % cup_list.list_length())

    for cup in cup_order:
        cup_list.add_list_item(cup)
        print("cup_list length: %i" % cup_list.list_length())
        cup_list.output_list()

    for move in range(1,move_count+1):
        print("="*80)
        print(f"Move {move} occuring!")

        next_cup = cup_list.unordered_search(cur_cup)
        print(f"next cup is {next_cup}")
        sec_next_cup = cup_list.unordered_search(next_cup)
        third_next_cup = cup_list.unordered_search(sec_next_cup)
        fourth_next_cup = cup_list.unordered_search(third_next_cup)
        
        destination_cup = cur_cup - 1
        valid = False
        picked_up_cups = []
        picked_up_cups.append(next_cup)
        picked_up_cups.append(sec_next_cup)
        picked_up_cups.append(third_next_cup)
        while not valid:
            if destination_cup == 0:
                    destination_cup = max_len+1
            elif destination_cup not in picked_up_cups:
                valid = True
            else: 
                destination_cup -= 1
        
        next_dest_cup = cup_list.unordered_search(destination_cup)

        cup_list.update_node(cur_cup, fourth_next_cup)
        cur_cup=fourth_next_cup
        print(f"Dest cup is {destination_cup}")
        cup_list.update_node(destination_cup, next_cup)
        cup_list.update_node(third_next_cup, next_dest_cup)
    
    cup_list.output_list
    #return cup_order

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []
    original_list = []

    #read each line and add to list
    for x in f:
        temp_str = x.strip()
        for num in temp_str:
            input_list.append(int(num))

    # PART 1
    part_1_list = input_list
    part_1_moves = 100
    part_1_max_len = len(part_1_list) - 1
    print(f"p1 length is {part_1_max_len}")
    print(f"Last num is: {part_1_list[part_1_max_len]}")
    p1_current_cup_index = 0  
    p1_current_cup = part_1_list[p1_current_cup_index]
    part_1_list = shuffle_cups(part_1_list, part_1_moves, part_1_max_len,p1_current_cup, p1_current_cup_index)

    p1_final_list = []
    p1_cup_one_idx = part_1_list.index(1)
    if p1_cup_one_idx == part_1_max_len:
        p1_final_list = part_1_list[0:len(part_1_list)]
    elif p1_cup_one_idx == 0:
        p1_final_list = part_1_list[1:]
    else:
        p1_final_list = part_1_list[p1_cup_one_idx+1:len(part_1_list)]
        p1_final_list.extend(part_1_list[0:p1_cup_one_idx])
   
    p1_final_string = ""
    for num in p1_final_list:
        p1_final_string = p1_final_string+str(num)
    print(p1_final_string)

    # PART 2
    # Need to implment Linked List because brute force is hella slow
    '''part_2_list = input_list
    part_2_moves = 10000000
    for x in range(10,1000001):
        part_2_list.append(int(x))
    part_2_max_len = len(part_2_list) - 1
    print(f"p2 length is {part_2_max_len}")
    print(f"Last num is: {part_2_list[part_2_max_len]}")
    p2_current_cup_index = 0
    p2_current_cup = part_2_list[p2_current_cup_index]
    part_2_list = shuffle_cups(part_2_list, part_2_moves, part_2_max_len, p2_current_cup, p2_current_cup_index)
   
    p2_cup_one_idx = part_2_list.index(1)
    neighbor_1 = part_2_list[p2_cup_one_idx+1]
    neighbor_2 = part_2_list[p2_cup_one_idx+2]
    print(f"N1 is {neighbor_1}, N2 is {neighbor_2}, product of them is: {neighbor_1*neighbor_2}")
    '''
if __name__ == "__main__":
    main()