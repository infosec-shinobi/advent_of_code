class BingoCard():

    def __init__(self, board_data, name):
        self.name = name
        self.board = board_data
        #self.hit_board = {"r1":0, "r2"}
        self.row_count ={1:0,2:0,3:0,4:0,5:0}
        self.column_count ={1:0,2:0,3:0,4:0,5:0}
        self.rows = {1:[],2:[],3:[],4:[],5:[]}
        self.columns = {1:[],2:[],3:[],4:[],5:[]}
        self.unhit_total = 0
        self.make_board(board_data)
        
    
    def make_board(self, data):
        
        row = 1
        column = 1

        for item in data:
            column = 1
            for num in item:
                self.unhit_total += int(num)
                self.rows[row].append(num)
                self.columns[column].append(num)
                column+=1
            row+=1
        print(self.rows)
        print(self.columns)

    def check_hit(self, drawn_num):

        for key, value in self.rows.items():
            if drawn_num in value:
                 self.row_count[key] +=1
                 self.unhit_total -= int(drawn_num)
        
        for key, value in self.columns.items():
            if drawn_num in value:
                 self.column_count[key] +=1

    def get_winning_list(self, list_type, key_num):
        if list_type == "row":
            return self.rows[key_num]
        else:
            return self.columns[key_num]

    def check_win(self, last_drawn):
        for key, value in self.row_count.items():
            if 5 == value:
                winning_list = self.get_winning_list("row",key)
                return True, "row", key, winning_list, last_drawn, self.name, self.unhit_total
        
        for key, value in self.column_count.items():
            if 5 == value:
                winning_list = self.get_winning_list("row",key)
                return True, "row", key, winning_list, last_drawn, self.name, self.unhit_total
        
        return False, False, False, False, False, self.name, self.unhit_total

    def print_data(self):
        #print(self.board)
        print(f"Rows: \n{self.rows}")
        print(f"Columns: \n{self.columns}")

drawn_values = []

with open('input.txt') as f:
#with open('ex.txt') as f:
    count = 1
    bingo_count = 1
    bingo_cards = []
    temp_card = []

    for line in f:
        line = line.rstrip()
        if count == 1:
            drawn_values = line.split(",")
            count+=1
        elif line == "":
            if count == 2:
                count+=1
                pass
            else:
                bingo_card_name = "card_"+str(bingo_count)
                bingo_card_name = BingoCard(temp_card, bingo_card_name)
                bingo_cards.append(bingo_card_name)
                
                temp_card = []
                bingo_count+=1
        else:
            line = line.split()
            temp_card.append(line)
    
    #create the last card
    bingo_card_name = "card_"+str(bingo_count)
    bingo_card_name = BingoCard(temp_card, bingo_card_name)
    bingo_cards.append(bingo_card_name)

#for item in bingo_cards:
#    print(item)
#    item.print_data()   

##########
# Part 1 #
##########

for num in drawn_values:
    print(num)
    for item in bingo_cards:
        item.print_data()
        item.check_hit(num)
        win_status, win_type, win_key, win_list, win_num, win_card, total_unhit = item.check_win(num)
 
        if win_status:
            break
    if win_status:
            break

print(f'Total unhit: {total_unhit}')
print(f"drawn num: {win_num}")
win_product = 0
win_product = int(total_unhit)*int(win_num)
print(f"Part 1: Winning Card {win_card}, winning match {win_type} {win_key}, answer: {win_product}")

##########
# Part 2 #
##########