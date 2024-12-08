import copy
import time

with open("input.txt", "r") as f:
    maze = [list(ln.strip()) for ln in f.readlines()]

def get_next(guard_pos, facing):
    match facing:
        case 0:
            nxt = (guard_pos[0] - 1, guard_pos[1])
        case 1:
            nxt = (guard_pos[0], guard_pos[1] + 1)
        case 2:
            nxt = (guard_pos[0] + 1, guard_pos[1])
        case _:
            nxt = (guard_pos[0], guard_pos[1] - 1)
    return nxt

for i, ln in enumerate(maze):
    try:
        guard_x = ln.index("^")
        og_guard_pos = (i, guard_x)
        break
    except ValueError:
        continue

bounds = (len(maze), len(maze[0]))

facing = 0
visited = set()
guard_pos = og_guard_pos
while 0 <= guard_pos[0] < bounds[0] and 0 <= guard_pos[1] < bounds[1]:
    visited.add(guard_pos[0]*bounds[1] + guard_pos[1])

    nxt = get_next(guard_pos, facing)

    try:
        match maze[nxt[0]][nxt[1]]:
            case "." | "^":
                guard_pos = nxt
            case "#":
                facing = (facing + 1) % 4
    except IndexError:
        break

print("Part 1:", len(visited))

t = time.time()
cycleable = 0
for v in visited:
    guard_pos = og_guard_pos
    facing = 0
    vpos = (v // bounds[1], v % bounds[1])
    newmaze = copy.deepcopy(maze)
    newmaze[vpos[0]][vpos[1]] = "O"
    cycle_counter = 0
    while 0 <= guard_pos[0] < bounds[0] and 0 <= guard_pos[1] < bounds[1]:
        nxt = get_next(guard_pos, facing)

        try:
            match newmaze[nxt[0]][nxt[1]]:
                case "." | "^":
                    guard_pos = nxt
                case "#" | "O":
                    facing = (facing + 1) % 4
        except IndexError:
            break

        if cycle_counter > len(maze)*len(maze[0]):
            cycleable += 1
            break
        cycle_counter += 1

print("Part 2:", cycleable)
print("Time for part 2:", time.time()-t, "s")