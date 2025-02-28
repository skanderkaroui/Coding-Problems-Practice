import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    current_max = max(a)
    res = []
    for __ in range(m):
        op, l, r = sys.stdin.readline().split()
        l = int(l)
        r = int(r)
        if op == '+':
            if l <= current_max <= r:
                current_max += 1
        else:
            if l <= current_max <= r:
                current_max -= 1
        res.append(current_max)
    print(' '.join(map(str, res)))