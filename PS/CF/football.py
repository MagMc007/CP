# https://codeforces.com/problemset/problem/43/A
# A. Football
from collections import Counter

n = int(input())
hash = Counter()


for _ in range(n):
    hash[input()] += 1

ans = ["", 0]

for k, v in hash.items():
    if v > ans[1]:
        ans = [k, v]
        
print(ans[0])