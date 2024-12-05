with open("input.txt", "r") as f:
    word_search = f.read().splitlines()

def extract_xmas(matrix: list[str], from_pos: tuple[int, int], direction):
    match direction:
        case 0:
            return [matrix[y][from_pos[1]] for y in range(from_pos[0], from_pos[0] - 4, -1) if y >= 0]
        case 1:
            return [matrix[y][x] for y, x in zip(range(from_pos[0], from_pos[0] - 4, -1), range(from_pos[1], from_pos[1] + 4)) if x >= 0 and y >= 0]
        case 2:
            return [matrix[from_pos[0]][from_pos[1]:from_pos[1] + 4]]
        case 3:
            return [matrix[y][x] for y, x in zip(range(from_pos[0], from_pos[0] + 4), range(from_pos[1], from_pos[1] + 4)) if x >= 0 and y >= 0]
        case 4:
            return [matrix[y][from_pos[1]] for y in range(from_pos[0], from_pos[0] + 4)]
        case 5:
            return [matrix[y][x] for y, x in zip(range(from_pos[0], from_pos[0] + 4), range(from_pos[1], from_pos[1] - 4, -1)) if x >= 0 and y >= 0]
        case 6:
            return [matrix[from_pos[0]][x] for x in range(from_pos[1], from_pos[1] - 4, -1) if x >= 0]
        case 7:
            return [matrix[y][x] for y, x in zip(range(from_pos[0], from_pos[0] - 4, -1), range(from_pos[1], from_pos[1] - 4, -1)) if x >= 0 and y >= 0]

def extract_mas(matrix: list[str], from_pos: tuple[int, int]):
    if (from_pos[0] - 1) < 0 or (from_pos[1] - 1) < 0:
        raise IndexError
    return ([matrix[from_pos[0]-1][from_pos[1]-1],
             matrix[from_pos[0]][from_pos[1]],
             matrix[from_pos[0]+1][from_pos[1]+1]],
            [matrix[from_pos[0]-1][from_pos[1]+1],
             matrix[from_pos[0]][from_pos[1]],
             matrix[from_pos[0]+1][from_pos[1]-1]])

counter = 0
counter2 = 0
for y in range(len(word_search)):
    for x in range(len(word_search[y])):
        if word_search[y][x] == "X":
            for direction in range(8):
                try:
                    xmas = "".join(extract_xmas(word_search, (y, x), direction))
                except IndexError:
                    continue
                if xmas == "XMAS" or xmas == "SAMX":
                    counter += 1
        if word_search[y][x] == "A":
            try:
                cross = ["".join(mas) for mas in extract_mas(word_search, (y, x))]
            except IndexError:
                continue
            if (cross[0] == "MAS" or cross[0] == "SAM") and (cross[1] == "MAS" or cross[1] == "SAM"):
                counter2 += 1


print("Part 1:", counter)
print("Part 2:", counter2)