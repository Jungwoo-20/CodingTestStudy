from collections import deque

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    res = 0
    dist = [[10000000000] * N for _ in range(N)]
    dist[0][0] = 0
    queue = deque()
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            _x = x + dx[i]
            _y = y + dy[i]
            if 0 <= _x < N and 0 <= _y < N:
                if dist[_x][_y] > matrix[_x][_y] + dist[x][y]:
                    dist[_x][_y] = matrix[_x][_y] + dist[x][y]
                    queue.append([_x, _y])
    print('#' + str(test_case) + ' ' + str(dist[N - 1][N - 1]))
