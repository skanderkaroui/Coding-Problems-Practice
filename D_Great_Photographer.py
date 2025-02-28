n, x_0 = map(int, input().split())

L = float('inf')
R = float('-inf')

for _ in range(n):
    a, b = map(int, input().split())
    low, high = min(a, b), max(a, b)

    R = max(R, low)
    L = min(L, high)

if R <= L:
    if R <= x_0 <= L:
        print(0)
    else:
        print(min(abs(x_0 - R), abs(x_0 - L)))
else:
    print(-1)
