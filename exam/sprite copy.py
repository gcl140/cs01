sprite = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
]

def invert(sprite):
    for row in sprite:
        for col in range(len(row)):
            if row[col] == 1:
                row[col] = 0
            else:
                row[col] = 1
    return sprite

print(sprite)
print(invert(sprite))