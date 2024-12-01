with open("input.txt", "r") as f:
    orig_pairs = [[int(x) for x in inp.split()] for inp in f.readlines()]

left = sorted([p[0] for p in orig_pairs])
right = sorted([p[1] for p in orig_pairs])

distances = [abs(l - r) for (l, r) in zip(left, right)]

print("Part 1:", sum(distances))

similarity = sum([(num * right.count(num)) for num in left])

print("Part 2:", similarity)