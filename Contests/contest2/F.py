from collections import Counter
n = int(input())

for _ in range(n):
    m = int(input())
    s = input()

    hash = Counter(s)
    leng = len(hash)
    ans = 0

    se = set()

    for i in range(m):
        se.add(s[i])
        hash[s[i]] -= 1
        if hash[s[i]] == 0:
            leng -= 1
        
        ans = max(ans, len(se)+leng)

    print(ans)
