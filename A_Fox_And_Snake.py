n, m = map(int, input().split())
matrix = [["."] * m for _ in range(n)]
right = True

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = "#"
    else:
        if right:
            matrix[i][-1] = "#"
            right = False
        else:
            matrix[i][0] = "#"
            right = True

for row in matrix:
    print(''.join(row))
