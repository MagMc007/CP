word = input()
upp_count = 0
low_count = 0
for char in word:
    if char.islower():
        low_count += 1
    else:
        upp_count += 1
if upp_count <= low_count:
    print(word.lower())
else:
    print(word.upper())