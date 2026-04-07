n, k = map(int, input().split())
from math import ceil
ans = 0
if n % 2 == 0:
    if k > n // 2: # in the even sector
        k -= n // 2
        ans = 2 + (k-1)*2
    else:
        ans = 1 + (k-1)*2
else:
    if k > ceil(n / 2):  # in the even sector
        k -= ceil(n/2)
        ans = 2 + (k-1)*2
    else:
        ans = 1 + (k-1)*2

print(ans)