import sys
from collections import deque

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]


def bfs(i, j):
    matrix[i][j] = 0
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < h and 0 <= _y < w and matrix[_x][_y] == 1:
                matrix[_x][_y] = 0
                queue.append((_x, _y))


while True:
    w, h = map(int, sys.stdin.readline().split())
    matrix = []
    res = 0
    if w == 0 and h == 0:
        break
    for _ in range(h):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i, j)
                res += 1
    print(res)
