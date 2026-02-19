shoes = list(map(int,input().split()))
shoes.sort()
buy = 0
for i in range(len(shoes)-1):
    if shoes[i] == shoes[i+1]:
        buy = buy + 1
print(buy)