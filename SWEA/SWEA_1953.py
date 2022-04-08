from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 1 상하좌우
# 2 상하
# 3 좌우
# 4 상우
# 5 하우
# 6 하좌
# 7 상좌

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
change = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append([R, C])
    visited[R][C] = 1
    while q:
        r, c = q.popleft()
        num = change[matrix[r][c]]
        if not num:
            continue
        for i in num:
            x, y = dx[i], dy[i]
            _x = r + x
            _y = c + y
            if 0 <= _x < N and 0 <= _y < M and not visited[_x][_y] and matrix[_x][_y] != 0:
                # 여기까지 전형적인 BFS 문제
                # 파이프가 있다고 모두 이동할 수 있는 것이 아니라
                # 이동한 위치에서 지금 내가 있는 위치로 돌아올 수 있는지 파악해야함(연결 여부 반드시 필요)
                # ex) 현재 위치가 상하좌우라도 이동할려는 곳의 파이프가 있지만 우하와 같은 경우에는 이동할 수 없다
                temp = change[matrix[_x][_y]]
                for te in temp:
                    t1, t2 = dx[te] + _x, dy[te] + _y
                    # 이동한 위치가 다시 내 자리로 돌아올 수 있으면 이동
                    if t1 == r and t2 == c:
                        q.append([_x, _y])
                        visited[_x][_y] = visited[r][c] + 1
                        break
    res = 0
    for i in range(N):
        for j in range(M):
            # L시간보다 작거나 같아야 함
            if 0 < visited[i][j] <= L:
                res += 1
    print('#' + str(test_case) + ' ' + str(res))
