n = int(input())
s = input()
res = []

for i in range(n-1, -1, -1):
    if len(res) <= 1:
        res.insert(0, s[i])
    else:
        mid = len(res) // 2
        if mid % 2 == 0:
            res.insert(mid, s[i])
        
        else:
            res.insert(mid, s[i])

print(''.join(res))
