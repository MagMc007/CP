n = int(input())
winner = input()
anton = 0
danik = 0
for letter in winner:
    if letter == "A":
        anton += 1
    else:
        danik += 1
if anton > danik:
    print("Anton")
elif anton < danik:
    print("Danik")
else:
    print("Friendship")