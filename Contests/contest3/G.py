arr1 = "qwertyuiopasdfghjkl;zxcvbnm,./"

shift = input()
read = input()

ans = ""

for i in read:
    idx = arr1.index(i)
    
    if shift == "R":
        ans += arr1[idx-1]
    else:
        ans += arr1[idx+1]

print(ans)