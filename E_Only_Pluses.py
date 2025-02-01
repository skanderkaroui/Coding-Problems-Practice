t = int(input())

for _ in range(t):
    a, b, c = list(map(int,input().split()))
    i = 0
    while i < 5:
        if a <= b <= c or a <= c <= b:
            a += 1
            i += 1
        elif b <= a <= c or b <= c <= a:
            b += 1
            i += 1
        else:
            c += 1
            i += 1

    print(a * b * c)
