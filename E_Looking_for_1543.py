t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    matrix = [[i] for i in input().split() for j in range(m)]


    i, j = 0, 0

    for k in range(n // 2):
        if matrix[i + k][j + k + 1]:
            