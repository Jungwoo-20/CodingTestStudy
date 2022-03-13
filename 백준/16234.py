import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
res = 0


def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    tmp = []
    # tmp 길이만큼 방문할 수 있다는 정보를 남기기 위함
    tmp.append([i, j])
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            _x = x + dx[idx]
            _y = y + dy[idx]
            if 0 <= _x < N and 0 <= _y < N and not visit[_x][_y]:
                if L <= abs(matrix[x][y] - matrix[_x][_y]) <= R:
                    visit[_x][_y] = True
                    queue.append([_x, _y])
                    tmp.append([_x, _y])
    return tmp


while True:
    visit = [[False] * N for _ in range(N)]
    isTrue = False
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j] = True
                temp = bfs(i, j)
                if len(temp) > 1:
                    isTrue = True
                    # 방문 값의 정보를 모두 합하고 연합의 수로 나누어 정보를 저장함
                    num = sum([matrix[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        matrix[x][y] = num
    # 연합을 만들 수 없는 경우였다면 탈출함
    if not isTrue:
        break
    res += 1
print(res)
