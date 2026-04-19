# https://codeforces.com/problemset/problem/4/C
# C. Registration system
n = int(input())

hash = {}
for _ in range(n):
    name = input().strip()

    if name in hash:
        print(f'{name}{hash[name]}')
        hash[name] += 1
    else:
        hash[name] = 1
        print('OK')
