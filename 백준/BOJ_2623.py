import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [[] * (N + 1) for _ in range(N + 1)]
isDegree = [0] * (N + 1)

for _ in range(M):
    lst = list(map(int, sys.stdin.readline().split()))
    for i in range(1, lst[0]):
        matrix[lst[i]].append(lst[i + 1])
        isDegree[lst[i + 1]] += 1
q = deque()
for i in range(1, N + 1):
    if isDegree[i] == 0:
        q.append(i)
res = []
while q:
    value = q.popleft()
    res.append(value)
    for i in matrix[value]:
        isDegree[i] -= 1
        if isDegree[i] == 0:
            q.append(i)

if len(res) == N:
    for i in res:
        print(i)
else:
    print(0)
