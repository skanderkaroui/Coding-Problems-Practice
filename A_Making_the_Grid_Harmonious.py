def min_moves(matrix):
    i_row, j_row = 0, 0

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                i_row, j_row = i, j
    
    return abs(i_row - 2) + abs(j_row - 2)


import sys

def min_moves(matrix):
    i_row, j_row = 0, 0

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                i_row, j_row = i, j
    
    return abs(i_row - 2) + abs(j_row - 2)

lines = sys.stdin.readlines()
matrix = []
for line in lines:
    row = list(map(int, line.split()))
    matrix.append(row)

print(min_moves(matrix))
