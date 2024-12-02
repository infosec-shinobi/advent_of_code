
def checks(report):
    start = report[0]
    for num in report[1:]:
        if abs(num - start) < 1 or abs(num - start) > 3:
            return "unsafe"
        start = num
    fwd_sort = sorted(report)
    reverse_sort = sorted(report, reverse=True)

    if report == fwd_sort or report == reverse_sort:
        return "safe"
    
    return "unsafe"

findings = {
    "safe": [],
    "unsafe": []
}

#with open('../../../input/2024/02/ex.txt') as f:
with open('../../../input/2024/02/input.txt') as f:
    for line in f:
        line = [int(x) for x in line.strip().split()]
        result = checks(line)
        findings[result].append(line)

print(len(findings["safe"]))