import sys

n, m = map(int, sys.stdin.readline().split())
matrix = [[0] * m for _ in range(n)]
matrix[0][0] = 1
for i in range(n):
    for j in range(m):
        _i = i + 1
        _j = j + 1
        if 0 <= _i < n:
            matrix[_i][j] += matrix[i][j]
        if 0 <= _j < m:
            matrix[i][_j] += matrix[i][j]
        if 0 <= _i < n and 0 <= _j < m:
            matrix[_i][_j] += matrix[i][j]
print(matrix[-1][-1] % 1000000007)
