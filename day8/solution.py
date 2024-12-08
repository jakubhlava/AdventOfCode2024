from itertools import product

import numpy as np

with open("input.txt", "r") as f:
    antmap = f.read().splitlines()

def hashable_point(point, bounds):
    return point[0]*bounds[1] + point[1]

bounds = (len(antmap), len(antmap[0]))
antennas = []
for y in range(len(antmap)):
    for x in range(len(antmap[0])):
        if antmap[y][x] != ".":
            antennas.append((antmap[y][x], (y,x)))

freqs = {f: [np.array(a[1]) for a in antennas if f == a[0]] for f in [a[0] for a in antennas]}

antinodes = set()
antinodes_p2 = set()
for f, ants in freqs.items():
    for ant in ants:
        antinodes_p2.add(hashable_point(ant, bounds))
    combinations = [p for p in product(ants, repeat=2) if p[0] is not p[1]]
    for c in combinations:
        base_vec = c[1] - c[0]
        antinode = c[1] + base_vec
        if all(0 <= v < bounds[0] for v in antinode):
            hashable = hashable_point(antinode, bounds)
            antinodes.add(hashable)
            antinodes_p2.add(hashable)
            possible_antinode = antinode
            while True:
                possible_antinode = possible_antinode + base_vec
                if all(0 <= v < bounds[0] for v in possible_antinode):
                    antinodes_p2.add(hashable_point(possible_antinode, bounds))
                else:
                    break

print("Part 1:", len(antinodes))
print("Part 2:", len(antinodes_p2))
