import sys
from copy import deepcopy
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 1


def ocean(x, y):
    cnt = 0
    for io in range(4):
        _x = x + dx[io]
        _y = y + dy[io]
        if 0 <= _x < N and 0 <= _y < M and tmp[_x][_y] == 0:
            cnt += 1
    return cnt


def bfs(_i, _j):
    visited[_i][_j] = True
    queue = deque()
    queue.append([_i, _j])
    while queue:
        x, y = queue.popleft()
        for ic in range(4):
            _x = x + dx[ic]
            _y = y + dy[ic]
            if 0 <= _x < N and 0 <= y < M and not visited[_x][_y] and matrix[_x][_y] != 0:
                visited[_x][_y] = True
                queue.append([_x, _y])


while True:
    visited = [[False] * M for _ in range(N)]
    sector = 0
    flag = True
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                flag = False
    # 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.
    if flag:
        print(0)
        break
    # 하나의 빙하를 녹이고 다음 빙하로 접근할 경우 인접 바다의 개수에서 차이가 발생함 그렇기 때문에 복사 한 다음에 접근
    tmp = deepcopy(matrix)
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            # 바다가 아닌 경우
            if tmp[i][j] != 0:
                # 현재 빙하의 크기에서 현재 인덱스의 인접 바다의 개수를 차감한 값을 저장
                matrix[i][j] = max(0, matrix[i][j] - ocean(i, j))
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            # 방문하지 않고 바다가 아닌 경우 bfs를 통해서 구역 개수를 카운
            if not visited[i][j] and matrix[i][j] != 0:
                bfs(i, j)
                sector += 1
    if sector >= 2:
        print(res)
        break
    res += 1
