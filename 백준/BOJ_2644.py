import sys
from collections import deque

n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

matrix = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x].append(y)
    matrix[y].append(x)
visited = [0] * (n + 1)
q = deque()
q.append(start)
visited[start] = 1


def bfs():
    while q:
        point_s = q.popleft()
        if point_s == end:
            print(visited[point_s] - 1)
            sys.exit()
        for i in matrix[point_s]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[point_s] + 1
    print(-1)

bfs()
