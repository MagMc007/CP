lamak, bob = list(map(int, input().split()))
year = 0
while lamak <= bob:
    lamak *= 3
    bob *= 2
    year += 1
print(year)
