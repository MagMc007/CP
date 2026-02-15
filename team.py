n = int(input())
possibility = ["1 1 1", "1 1 0", "1 0 1", 
                "0 1 1"]
implement = 0
for i in range(n):
    response = input()
    if response in possibility:
        implement += 1
print(implement)