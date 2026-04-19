# https://codeforces.com/problemset/problem/2/A
# A. Winner
from collections import Counter

n = int(input())
hash = Counter()
n_s = []

for _ in range(n):
    name, score = input().split()
    score = int(score)
    hash[name] += score
    n_s.append([name, score])

max_score = max(hash.values())

# identify those who may win
may_win = set()
for k, v in hash.items():
    if v == max_score:
        may_win.add(k)

# separe the one who got to max first
hash2 = Counter()

for n, s in n_s:
    if n in may_win:
        hash2[n] += s

        if hash2[n] >= max_score:
            print(n)
            break
