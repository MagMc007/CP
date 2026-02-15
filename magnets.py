n = int(input())
magnet = []
group = 1
for i in range(n):
    magnet.append(input())
    if magnet[i] != magnet[i-1]:
        group += 1

print(group)
