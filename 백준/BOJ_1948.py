import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
matrix = [[] * (n + 1) for _ in range(n + 1)]
matrix_R = [[] * (n + 1) for _ in range(n + 1)]
isDegree = [0] * (n + 1)

for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    matrix[start].append([end, weight])
    matrix_R[end].append([start, weight])
    isDegree[end] += 1
start, end = map(int, sys.stdin.readline().split())

q = deque()
q.append([start, 0])
dist = [0] * (n + 1)

while q:
    start, weight = q.popleft()
    for i, j in matrix[start]:
        isDegree[i] -= 1
        # 모두가 만날 수 있는 최소 시간을 구해야 하기 때문에 시간은 최대가 되어야 함
        dist[i] = max(dist[i], weight + j)
        if isDegree[i] == 0:
            q.append([i, dist[i]])

q = deque()
q.append(end)

visited = [0] * (n + 1)
visited[end] = 1
cnt = 0
while q:
    end1 = q.popleft()
    for i, j in matrix_R[end1]:
        # 지나왔던 도로인지 확인해서 같은 경우는 카운트 증가
        if j + dist[i] == dist[end1]:
            cnt += 1
            if not visited[i]:
                q.append(i)
                visited[i] = 1
print(dist[end])
print(cnt)
