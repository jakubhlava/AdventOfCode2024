import re

with open("input.txt", "r") as f:
    memory = f.read()

instructions = list(re.finditer(r"mul\((\d+),(\d+)\)", memory))

print("Part 1:", sum(int(m.group(1)) * int(m.group(2)) for m in instructions))

dos = sorted([d.start() for d in re.finditer(r"do\(\)", memory)])
donts = sorted([d.start() for d in re.finditer(r"don't\(\)", memory)])
p2_enabled = []
for i in instructions:
    closest_do = [d for d in dos if d < i.start()]
    closest_dont = [d for d in donts if d < i.start()]

    if len(closest_dont) > 0 and ((len(closest_do) > 0 and closest_do[-1] < closest_dont[-1]) or len(closest_do) == 0):
        continue

    p2_enabled.append(i)

print("Part 2:", sum(int(m.group(1)) * int(m.group(2)) for m in p2_enabled))
