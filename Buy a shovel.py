k, r = list(map(int, input().split()))
bought = 1
initial = k
change = None
while change != 0:
    if initial%10 == 0:
        change = 0
    elif (initial%10) - r == 0:
        change = 0
    else:
        initial += k
        bought += 1

print(bought)
