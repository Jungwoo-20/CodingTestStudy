import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

matrix = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
visited[X] = 0
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    matrix[A].append(B)
queue = deque([X])

while queue:
    x = queue.popleft()
    for i in matrix[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            queue.append(i)
res = []
for i in range(N + 1):
    if visited[i] == K:
        print(i)
if K not in visited:
    print(-1)
