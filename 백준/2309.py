import sys

matrix = []
one = 0
two = 0
for _ in range(9):
    matrix.append(int(sys.stdin.readline()))
sumM = sum(matrix)
for i in range(8):
    for j in range(i + 1, 9):
        if sumM - (matrix[i] + matrix[j]) == 100:
            one = matrix[i]
            two = matrix[j]
matrix.remove(one)
matrix.remove(two)
matrix.sort()
for i in matrix:
    print(i)