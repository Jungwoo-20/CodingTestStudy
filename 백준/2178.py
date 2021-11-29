import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

matrix = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))

queue = deque()
queue.append((0, 0))
matrix[0][0] = 1
while queue:
    x, y = queue.popleft()
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0 <= _x < N and 0 <= _y < M and matrix[_x][_y] == 1:
            matrix[_x][_y] = matrix[x][y]+1
            queue.append((_x,_y))
print(matrix[N-1][M-1])
