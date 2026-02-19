wire = int(input())   #n
osklo = list(map(int, input().split())) #a
shot = int(input())  #m

for _ in range(shot):
    x, y = list(map(int, input().split()))
    x = x-1
    if x > 0:
        osklo[x-1] += y - 1
    if x < wire - 1:
        osklo[x + 1] += osklo[x] - y
    osklo[x] = 0

for osk in osklo:
    print(osk)
