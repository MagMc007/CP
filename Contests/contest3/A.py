# https://codeforces.com/contests/684115

n = int(input())
arr = list(map(int, input().split()))

dic = {0:0, 1:0, 2:0}

for i in range(n):
    dic[i % 3] += arr[i]
mx = 0
ans = None

for k, v in dic.items():
    if v > mx:
        ans = k
        mx = v

if ans == 0:
    print("chest")
elif ans == 1:
    print("biceps")
else:
    print("back")

