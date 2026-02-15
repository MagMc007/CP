n = int(input())
home = []
away = []
change = 0
for i in range(n):
    ho, aw = list(map(int, input().split()))
    home.append(ho)
    away.append(aw)
for i in home:
    change += away.count(i)
print(change)
