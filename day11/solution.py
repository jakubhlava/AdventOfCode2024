from collections import Counter, defaultdict

with open("input.txt", "r") as f:
    stones = [s for s in f.read().strip().split()]

dict_stones = dict(Counter(stones))
for cycle in range(75):
    if cycle == 25:
        print("Part 1:", sum(dict_stones.values()))
    newstones = defaultdict(int)
    for stone in dict_stones.keys():
        if stone == "0":
            newstones["1"] += dict_stones[stone]
        elif len(stone) % 2 == 0:
            new = [stone[:len(stone) // 2], str(int(stone[len(stone) // 2:]))]
            for key in new:
                newstones[key] += dict_stones[stone]
        else:
            newstones[str(int(stone) * 2024)] += dict_stones[stone]
    dict_stones = newstones

print("Part 2:", sum(dict_stones.values()))
