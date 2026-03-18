na, nb = map(int, input().split())
k, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


a = a[k-1]  # biggests in a
b = b[nb-m] 

if a < b:
    print("YES")
else:
    print("NO")