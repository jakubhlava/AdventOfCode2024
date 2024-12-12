with open("input.txt", "r") as f:
    trailmap = [[int(x) for x in ln] for ln in f.read().splitlines()]

def neighbors(pt):
    possible = [(pt[0] + 1, pt[1]), (pt[0], pt[1] + 1), (pt[0] - 1, pt[1]), (pt[0], pt[1] - 1)]
    return [p for p in possible if p[0] >= 0 and p[1] >= 0]

starting = []
for y in range(len(trailmap)):
    for x in range(len(trailmap[0])):
        if trailmap[y][x] == 0:
            starting.append((y, x))

scores = []
total_trails = 0
for sp in starting:
    peaks = set()
    trails = 0
    stack = [sp]
    while len(stack) > 0:
        curr = stack.pop()
        neighb_list = neighbors(curr)
        for n in neighb_list:
            try:
                if trailmap[n[0]][n[1]] - trailmap[curr[0]][curr[1]] == 1:
                    stack.append(n)
            except IndexError:
                pass
        if trailmap[curr[0]][curr[1]] == 9:
            peaks.add(curr[0] * len(trailmap[0]) + curr[1])
            trails += 1
    scores.append(len(peaks))
    total_trails += trails

print("Part 1:", sum(scores))
print("Part 2:", total_trails)