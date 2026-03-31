n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
s = sum(a)

curr = 0
numb = 0

for i in a:
    curr += i
    numb += 1
    if curr > s - curr:
        print(numb)
        break
    
    

print("NO")