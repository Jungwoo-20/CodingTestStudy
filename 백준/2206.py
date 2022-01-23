import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def bfs(start, end, wall, matrix, visited):
    q = deque()
    q.append((start, end, wall))
    visited[start][end][wall] = 1
    while q:
        x, y, _wall = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][_wall]
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            # 배열 범위 벗어남
            if _x < 0 or _x >= N or _y < 0 or _y >= M:
                continue
            # 그 외
            if visited[_x][_y][_wall] == 0 and matrix[_x][_y] == 0:
                visited[_x][_y][_wall] = visited[x][y][_wall] + 1
                q.append((_x, _y, _wall))
            # 벽 부수는 조건
            if _wall == 0 and matrix[_x][_y] == 1:
                visited[_x][_y][_wall + 1] = visited[x][y][_wall] + 1
                q.append((_x, _y, _wall + 1))
    return -1


print(bfs(0, 0, 0, matrix, visited))
