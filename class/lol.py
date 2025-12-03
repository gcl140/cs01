schemes = [
    ["gray", "green", "blue"],
    ["red", "yellow", "purple"],
    ["cyan", "magenta", "lime"],
    ["orange", "pink", "teal"],
    ["brown", "black", "white"]
]

schemes.append(["navy", "maroon", "olive"])
print(schemes[1])
print(schemes[1][1])
print(schemes)
for row in schemes:
    for col in row:
        print(col)

# Different order of string printing
for c in range(len(schemes[0])):
    for r in range(len(schemes)):
        print(schemes[c][r])