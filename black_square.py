clrylist = list(map(int, input().split()))
position = input()
calories = 0
for i in position:
    i = int(i) - 1
    calories += clrylist[i]
print(calories)
