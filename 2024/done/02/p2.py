
def checks(report):
    start = report[0]
    for num in report[1:]:
        if abs(num - start) < 1 or abs(num - start) > 3:
            return "recheck"
        start = num
    fwd_sort = sorted(report)
    reverse_sort = sorted(report, reverse=True)

    if report == fwd_sort or report == reverse_sort:
        return "safe"
    
    return "recheck"

findings = {
    "safe": [],
    "recheck": [],
    "unsafe": []
}

#with open('../../../input/2024/02/ex.txt') as f:
with open('../../../input/2024/02/input.txt') as f:
    for line in f:
        line = [int(x) for x in line.strip().split()]
        result = checks(line)
        findings[result].append(line)

print(f"undampend: {len(findings['safe'])}")

for report in findings["recheck"]:
    safe = False
    for x in range(0,len(report)):
        new_report = report.copy()
        new_report.pop(x)
        new_finding = checks(new_report)
        if new_finding == "safe":
            safe = True
    if safe:
        findings["safe"].append(report)
    else:
        findings["unsafe"].append(report)

print(f"dampened: {len(findings['safe'])}")