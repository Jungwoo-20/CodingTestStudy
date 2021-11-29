import sys

sys.setrecursionlimit(10 ** 8)

N, M = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0


def dfs(i):
    visited[i] = True
    for e in matrix[i]:
        if not visited[e]:
            dfs(e)


for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    matrix[u].append(v)
    matrix[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
