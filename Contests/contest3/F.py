t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    odds = 0
    for i in arr:
        if i % 2 != 0:
            odds += 1
    
    if odds == 0:
        print("No")
    elif x == n:
        if odds % 2 == 1:g
            print("Yes")
        else:
            print("No")
    else:
        if odds == n and x % 2 == 0:
            print("No")
        else:
            print("Yes")
   
