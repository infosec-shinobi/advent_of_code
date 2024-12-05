import math

rules = {}
pages = []

reading_rules = True
#with open('../../../input/2024/05/ex.txt') as f:
with open('../../../input/2024/05/input.txt') as f:
    for line in f:
        if line.strip() == "":
            reading_rules = False
        elif reading_rules:
            nums = line.strip().split("|")
            rules.setdefault(int(nums[0]), []).append(int(nums[1]))
        else:
            temp_list = line.strip().split()
            pages.append([int(x) for x in line.strip().split(",")])

valid_orders = []
for page in pages:
    reviewed_page_num = []
    violation = False
    
    for item in page:
        check_nums = rules.get(int(item), [])
        violations = set(check_nums).intersection(set(reviewed_page_num))
        reviewed_page_num.append(item)
        if violations:
            violation = True
            break
    if not violation:
        valid_orders.append(page)

total = 0
for orders in valid_orders:
    middle = math.floor(len(orders)/2)
    total += orders[middle]
print(total)