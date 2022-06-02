T = int(input())


def dfs(start, end, value):
    global result
    if value <= result:
        return
    if start == end:
        if value > result:
            result = value
            return
    for i in range(N):
        if not visited[i]:
            tmp = value * matrix[start][i] * 0.01
            visited[i] = 1
            dfs(start + 1, end, tmp)
            visited[i] = 0


for tc in range(1, T + 1):
    N = int(input())
    matrix = []
    visited = [0] * N
    result = -1
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    dfs(0, N, 1)
    result *= 100
    print('#' + str(tc) + ' ' + '%.6f' % result)
