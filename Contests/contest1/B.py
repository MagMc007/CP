from math import ceil
n, k = map(int, input().split())

h = ceil(n / 2)

if k <= h:
    print(2 * k - 1)
else:
    print(2* (k-h))