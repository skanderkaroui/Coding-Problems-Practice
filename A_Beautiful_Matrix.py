mat = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            pos = (i, j)

print(abs(pos[0] - 2) + abs(pos[1] - 2))
