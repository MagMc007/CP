t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    evencnt = 0
    oddcnt = 0

    for i in arr:
        if i % 2 == 0:
            evencnt += 1
        else:
            oddcnt += 1
    
    if oddcnt % 2 != 0:
        print("YES")
    elif oddcnt and evencnt:
        print("YES")
    else:
        print("NO")

