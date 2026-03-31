t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    total = 0
    neg_count = 0
    min_abs_val = 101

    for _ in range(n):
        row = list(map(int, input().split()))
        for val in row:
            total += abs(val)

            if val < 0:
                neg_count += 1
            
            if abs(val) < min_abs_val:
                min_abs_val = abs(val)
    
    if neg_count % 2 == 0:
        print(total)
    else:
        print(total - 2 * min_abs_val)