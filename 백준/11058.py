import sys

n = int(sys.stdin.readline())
matrix = [i for i in range(0, 102)]
for i in range(6, 101):
    matrix[i] = max(matrix[i - 3] * 2, max(matrix[i - 4] * 3, matrix[i - 5] * 4))
print(matrix[n])
