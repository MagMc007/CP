row = None
column = None
entries = 0
for i in range(5):
    entry = input().split()
    entries += 1
    if "1" in entry:
        row = entries
        place = entry.index("1")
        column = place + 1
moves = 0
while row != 3:
    if row < 3:
        row += 1
    else:
        row -= 1
    moves += 1
while column != 3:
    if column < 3:
        column += 1
    else:
        column -= 1
    moves += 1

print(moves)