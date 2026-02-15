name = input()
chars = []
for i in name:
    if not i in chars:
        chars.append(i)
if len(chars)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM")