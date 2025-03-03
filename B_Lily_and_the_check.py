t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    count = 0

    while y > 0:
        if y < x:
            count += y
            y = 0
            
        else:
            p = 0
            while x * 10 ** p <= y:
                p += 1
            p -= 1
            a = x * 10 ** p
            count += y // a
            y %= a
    print(count)
