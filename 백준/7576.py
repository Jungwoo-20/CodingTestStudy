import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
queue = deque()  # 꼭 deque를 쓰지 않아도 됨

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0 <= _x < N and 0 <= _y < M and matrix[_x][_y] == 0:
            matrix[_x][_y] = matrix[x][y] + 1
            queue.append([_x, _y])
flag = False
result = -2
for i in matrix:
    for j in i:
        if j == 0:
            flag = True
        result = max(result, j)

if flag:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
