name = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
start_alp = "a"
start_indx = 0
rotations = 0
for char in name:
    end = alphabet.index(char)
    clockwise = abs(end - start_indx)
    anti_clockwise = 26 - clockwise
    rotations += min(clockwise, anti_clockwise)
    start_indx = end

print(rotations)