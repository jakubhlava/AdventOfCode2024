with open("input.txt", "r") as f:
    diskmap = [int(x) for x in f.read().strip()]

blocks = []
files = []
free = False
id = 0
for d in diskmap:
    if free:
        blocks.extend(["." for _ in range(d)])
        files.append(("free", d))
    else:
        blocks.extend([id for _ in range(d)])
        files.append(("file", d, id))
        id += 1
    free = not free

free_indices = [i for i, blk in enumerate(blocks) if blk == "." and i < len(blocks) - blocks.count(".")]
for i in range(len(blocks)-1, 0, -1):
    if blocks[i] != ".":
        try:
            free = free_indices.pop(0)
        except IndexError:
            break
        blocks[free] = blocks[i]
        blocks[i] = "."

print("Part 1:", sum(i*v for i, v in enumerate(blocks) if type(v) == int))

for i in range(len(files)-1, 0, -1):
    if files[i][0] == "file":
        for j in range(i):
            if files[j][0] == "free" and files[j][1] >= files[i][1]:
                residue = files[j][1] - files[i][1]
                files[j] = files[i]
                files[i] = ("free", files[i][1])
                if residue > 0:
                    if files[j+1][0] == "free":
                        files[j+1] = ("free", files[j+1][1] + residue)
                    else:
                        files.insert(j+1, ("free", residue))
                break

p2blks = []
for f in files:
    if f[0] == "free":
        p2blks.extend(["." for _ in range(f[1])])
    else:
        p2blks.extend([f[2] for _ in range(f[1])])

print("Part 2:", sum(i*v for i, v in enumerate(p2blks) if type(v) == int))
