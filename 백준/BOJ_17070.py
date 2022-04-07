import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

# 0은 가로, 1은 세로, 2는 대각
dp[0][0][1] = 1 # 최초 상태의 방향은 가로로 차지하고 있음
for i in range(2, N):
    if matrix[0][i] != 1: # 가장 윗 행에서 시작하기 때문에 벽이 아닌 경우에는 이전 값으로 초기화
        dp[0][0][i] = dp[0][0][i - 1]

# 탐색
for i in range(1, N):
    for j in range(1, N):
        # 대각선에서 올 수 있는 경우
        if matrix[i][j] == 0 and matrix[i - 1][j] == 0 and matrix[i][j - 1] == 0:
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
        if matrix[i][j] == 0:
            # 세로에서 올 수 있는 경우
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
            # 가로로 올 수 있는 경우
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]

# 가로 세로 대각선에서 올 수 있는 모든 경우 합산하여 결과 출력
print(sum(dp[i][N - 1][N - 1] for i in range(3)))
