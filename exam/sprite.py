sprite = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
]

# def invert(sprite):
#     for row in sprite:
#         for col in range(len(row)):
#             if row[col] == 1:
#                 row[col] = 0
#             else:
#                 row[col] = 1
#     return sprite

def invert(sprite):
    for row in sprite:
        for col in row:
            if col == 1:
                print(col)
                # row[col] = 0
            else:
                # row[col] = 1
                str(1)+"p"
    return sprite

def swap(sprite, r1, c1, r2, c2):
    sprite[r1][c1], sprite[r2][c2] = sprite[r2][c2], sprite[r1][c1]
    return sprite

def swap(sprite, r1, c1, r2, c2):
    for r in range(len(sprite)):
        if r == r1:
            for c in range(len(sprite[r])):
                if c == c1:
                    temp = sprite[r][c]
                    for rr in range(len(sprite)):
                        if rr == r2:
                            for cc in range(len(sprite[rr])):
                                if cc == c2:
                                    sprite[r][c] = sprite[rr][cc]
                                    sprite[rr][cc] = temp
    return sprite

def short_swap(sprite, r1, c1, r2, c2):
    sprite[r1][c1], sprite[r2][c2] = sprite[r2][c2], sprite[r1][c1]
    return sprite


# def flip_horizontal(sprite):
#     for row in range(len(sprite)):
#         # sprite[row].reverse()
#         for col in range(len(sprite[row]) // 2):
#             # swap(sprite, row, col, row, len(sprite[row]) - 1 - col)
#             short_swap(sprite, row, col, row, len(sprite[row]) - 1 - col)
#     return sprite

def flip_horizontal(sprite):
    for row in range(len(sprite)):
        for col in range(len(sprite[row]) // 2):
            short_swap(sprite, row, col, row, len(sprite[row]) - 1 - col)
    return sprite

print(sprite)
print(invert(sprite))
# print(swap(sprite, 0, 2, 4, 4))
# print(short_swap(sprite, 0, 2, 4, 4))
# print(flip_horizontal(sprite))