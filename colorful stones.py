s = input()
t = input()
ind = 0
for i in t:
    if i == s[ind]:
        ind += 1
print(ind+1)
