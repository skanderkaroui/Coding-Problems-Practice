t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))
    a, b, c = nums
    if (a == b + c) or (b == a + c) or (c == a + b):
        print("YES")
    else:
        print("NO")