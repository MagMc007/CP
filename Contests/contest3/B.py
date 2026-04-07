n = int(input())
arr = list(map(int, input().split()))

mx = max(arr)
mn = min(arr)


idxmn = n - 1 - arr[::-1].index(mn)
idxmx = arr.index(mx)

overlap = 1 if idxmx > idxmn else 0

moves = idxmx + n - 1 - idxmn - overlap
print(moves)
