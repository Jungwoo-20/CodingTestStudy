import sys

sys.setrecursionlimit(10**7)
M, N = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(M):
    matrix.append(list(map(int, sys.stdin.readline().split())))
visited = [[- 1 for _ in range(N)] for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1
    elif visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if 0 <= _x < M and 0 <= _y < N and matrix[_x][_y] < matrix[x][y]:
            visited[x][y] += dfs(_x, _y)
    return visited[x][y]


print(dfs(0, 0))
