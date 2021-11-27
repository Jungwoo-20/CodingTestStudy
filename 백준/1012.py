import sys
sys.setrecursionlimit(10000)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        if (0 <= px < N) and (0 <= py < M):
            if matrix[px][py] == 1:
                matrix[px][py] = -1
                dfs(px, py)


case = int(sys.stdin.readline())
for _ in range(case):
    M, N, K = map(int, sys.stdin.readline().split())
    matrix = [[0] * M for i in range(N)]
    res = 0
    for i in range(K):
        m, n = map(int, sys.stdin.readline().split())
        matrix[n][m] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                dfs(i, j)
                res += 1
    print(res)
