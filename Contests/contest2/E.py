m = int(input())
for i in range(m):
    n = int(input())

    ans = []
    for i in range(n, 0, -1):
        ans.append(i)

    print(*ans)