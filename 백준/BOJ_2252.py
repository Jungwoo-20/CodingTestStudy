import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [[] * (N + 1) for _ in range(N + 1)]
inDegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    # 대소 관계를 저장
    matrix[A].append(B)
    # 진출 차수의 목적지 부분 +1
    inDegree[B] += 1

q = deque()
for i in range(1, N + 1):
    # 진입 차수가 0인 경우 큐에 저장(선행 조건이 없기 때문에)
    if inDegree[i] == 0:
        q.append(i)

res = []
while q:
    value = q.popleft()
    res.append(value)
    # 갈 수 있는 곳
    for i in matrix[value]:
        # 진입 차수를 하나 줄이고
        inDegree[i] -= 1
        # 더이상 진입 차수가 필요업는 경우에는
        if inDegree[i] == 0:
            # 큐에 집어 넣어야 함
            q.append(i)
print(*res)
