n, k = map(int, input().split())

arr = list(map(int, input().split()))

s = 0
for i in range(k):
    s += arr[i]

min_ = s
ans = 0

i = 0

for j in range(k, n):

    s -= arr[i]
    s += arr[j]
    i += 1

    if s <= min_:
        ans = i
        min_ = s


print(ans + 1)
