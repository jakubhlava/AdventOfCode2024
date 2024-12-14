import re
from functools import reduce
from operator import mul

import png

value_regex = re.compile(r"-?[0-9]+")

with open("input.txt", "r") as f:
    robot_inputs = f.read().splitlines()
    robot_values = [[int(x) for x in value_regex.findall(inp)] for inp in robot_inputs]
    robots = [[(r[0], r[1]), (r[2], r[3])] for r in robot_values]

SIZE = (101, 103)

robots_history = []

for tick in range(20000):
    if tick == 100:
        quadrants = [
            [r for r in robots if r[0][0] < SIZE[0] // 2 and r[0][1] < SIZE[1] // 2],
            [r for r in robots if r[0][0] < SIZE[0] // 2 and r[0][1] > SIZE[1] // 2],
            [r for r in robots if r[0][0] > SIZE[0] // 2 and r[0][1] < SIZE[1] // 2],
            [r for r in robots if r[0][0] > SIZE[0] // 2 and r[0][1] > SIZE[1] // 2],
        ]

        print("Part 1:", reduce(mul, [len(q) for q in quadrants]))

    for robot in robots:
        new_pos = ((robot[0][0] + robot[1][0]) % SIZE[0], (robot[0][1] + robot[1][1]) % SIZE[1])
        robot[0] = new_pos

    # Numbers based on manual lookup for beginning of suspicious robot clusterings
    if (tick - 19) % 101 == 0 or (tick - 89) % 103 == 0:
        robot_positions = [r[0] for r in robots]
        array = [[255 if (x, y) in robot_positions else 0 for x in range(SIZE[0])] for y in range(SIZE[1])]

        png.from_array(array, "L").save(f"seconds/{tick + 1}.png")

    # Finally, manually check the output folder PNGs for the tree image
