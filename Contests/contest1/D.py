n = int(input())
arr = list(map(int, input().split()))

arr.sort()

if n < 3:
    print(0)
else:
    # remove the biggest
    val1 = arr[-2] - arr[0]

    # remove the smallest
    val2 = arr[-1] - arr[1]

    print(min(val1, val2))