t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    hashMap = {}

    for i in range(n):
        diff = arr[i] - i
        if diff in hashMap:
            count += hashMap[diff]
            hashMap[diff] += 1
        else:
            hashMap[diff] = 1
    print(count) 
