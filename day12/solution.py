from collections import defaultdict

with open("input.txt", "r") as f:
    garden = f.read().splitlines()


def get_neighbors(p):
    return [(p[0] + 1, p[1]), (p[0], p[1] + 1), (p[0] - 1, p[1]), (p[0], p[1] - 1)]


def is_out_of_bounds(p, g):
    return not (0 <= p[0] < len(g) and 0 <= p[1] < len(g[0]))


def get_valid_neighbors(p, g):
    return [pt for pt in get_neighbors(p) if not is_out_of_bounds(pt, g)]


def flattify_coord(p, g):
    return p[0] * len(g) + p[1]


visited = set()
groups: dict[str, list[list]] = defaultdict(list)

for y in range(len(garden)):
    for x in range(len(garden[y])):
        if flattify_coord((y, x), garden) in visited:
            continue

        visited.add(flattify_coord((y, x), garden))

        group = [(y, x)]
        group_letter = garden[y][x]
        stack = get_valid_neighbors((y, x), garden)
        while len(stack) > 0:
            pt = stack.pop(0)
            if flattify_coord(pt, garden) in visited:
                continue
            if garden[pt[0]][pt[1]] == group_letter:
                visited.add(flattify_coord(pt, garden))
                group.append(pt)
            # print(get_valid_neighbors(pt, garden))
            stack.extend([p for p in get_valid_neighbors(pt, garden) if
                          flattify_coord(p, garden) not in visited and garden[p[0]][p[1]] == group_letter])

        groups[group_letter].append(group)

# print(groups)

total = 0
for letter in groups.keys():
    regions = groups[letter]
    for region in regions:
        perimeter = 0
        for pt in region:
            neighbors = get_neighbors(pt)
            for n in neighbors:
                if is_out_of_bounds(n, garden) or garden[n[0]][n[1]] != letter:
                    perimeter += 1
        # print(region, len(region), perimeter)
        total += len(region) * perimeter


print("Part 1:", total)
