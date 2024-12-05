import math

def check_valid_order(unknown_ordered_pages,rule_dict):
    reviewed_page_num = []
    violation = False
    issue_index = "pickles"
    for index, item in enumerate(unknown_ordered_pages):
        check_nums = rules.get(int(item), [])
        violations = set(check_nums).intersection(set(reviewed_page_num))
        reviewed_page_num.append(item)
        if violations:
            violation = True
            issue_index = index
            break
    return violation, issue_index
        
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
invalid_order = []
for page in pages:
    issue, issue_index = check_valid_order(page,rules)
    if not issue:
        valid_orders.append(page)
    else:
        invalid_order.append(page)

corrected_order = []

for invalid in invalid_order:
    while True:
        issue, issue_index = check_valid_order(invalid,rules)
        if not issue:
            corrected_order.append(invalid)
            break
        else:
            removed_item = invalid.pop(issue_index)
            invalid.insert(issue_index-1, removed_item)

total = 0
for orders in corrected_order:
    middle = math.floor(len(orders)/2)
    total += orders[middle]
print(total)