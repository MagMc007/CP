# https://codeforces.com/gym/679478/problem/A
t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())

    a = input().split()
    b = input().split()
    c = input().split()
    all = Counter(a + b + c)
    score = [0, 0, 0]
    # print(all)
    for i in range(n):
        # a
        curr = a[i]
        cnt = all[curr]

        if cnt == 2:
            score[0] += 1
        
        if cnt == 1:
            score[0] += 3
        
        # b
        curr = b[i]
        cnt = all[curr]

        if cnt == 2:
            score[1] += 1
        
        if cnt == 1:
            score[1] += 3
        
        # c
        curr = c[i]
        cnt = all[curr]

        if cnt == 2:
            score[2] += 1
        
        if cnt == 1:
            score[2] += 3
    print(*score)
