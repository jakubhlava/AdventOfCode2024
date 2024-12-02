from itertools import pairwise

def check_report(paired_report):
    diff = [p[0] - p[1] for p in paired_report]
    limits = [1 <= abs(d) <= 3 for d in diff]
    decrease = [d > 0 for d in diff]
    increase = [d < 0 for d in diff]
    return (all(decrease) or all(increase)) and all(limits)


with open("input.txt", "r") as f:
    reports = [[int(num) for num in x.split()] for x in f.readlines()]

safe = 0
safe_p2 = 0

for report in reports:
    paired_report = list(pairwise(report))
    if check_report(paired_report):
        safe += 1
        safe_p2 += 1
    else:
        variants = [
            [level for i, level in enumerate(report) if i != j]
            for j in range(len(report))
        ]
        if any([check_report(list(pairwise(v))) for v in variants]):
            safe_p2 += 1

print("Part 1:", safe)
print("Part 2:", safe_p2)