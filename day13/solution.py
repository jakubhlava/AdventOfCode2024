import math
import re

with open("input-sm.txt", "r") as f:
    machine_inputs = f.read().split("\n\n")
    machines = [m.splitlines() for m in machine_inputs]

xy_regex = re.compile(r"[0-9]+")

tokens = 0
for machine in machines:
    Axy = [int(n) for n in xy_regex.findall(machine[0])]
    Bxy = [int(n) for n in xy_regex.findall(machine[1])]
    prizexy = [int(n) for n in xy_regex.findall(machine[2])]

    possible_combinations = []
    for i in range(101):
        for j in range(101):
            if i*Axy[0] + j*Bxy[0] == prizexy[0]:
                possible_combinations.append((i, j))

    if len(possible_combinations) == 0:
        continue

    real_combinations = []
    for pc in possible_combinations:
        if pc[0] * Axy[1] + pc[1] * Bxy[1] == prizexy[1]:
            real_combinations.append(pc)

    comb_tokens = [3*rc[0] + rc[1] for rc in real_combinations]
    try:
        tokens += min(comb_tokens)
    except ValueError:
        pass

    print(math.gcd(Axy[0], Bxy[0]))
    print(math.lcm(Axy[0], Bxy[0]))
    print(Axy, Bxy, prizexy, possible_combinations, real_combinations, comb_tokens)



print("Part 1:", tokens)