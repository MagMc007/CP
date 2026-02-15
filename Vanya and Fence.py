n, h = list(map(int, input().split()))
height = list(map(int, input().split()))
counter = 0
for person in height:
    if person > h:
        counter += 2
    else:
        counter +=1
print(counter)