import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    # 세 정수 A, B(1 ≤ A, B ≤ N)
    A, B, C = map(int, sys.stdin.readline().split())
    matrix[A].append([B, C])
    matrix[B].append([A, C])

# 공장이 있는 두 섬을 연결
start, end = map(int, sys.stdin.readline().split())

# C(1 ≤ C ≤ 1,000,000,000)
c_min, c_max = 1, 1000000000

res = c_min


def bfs(mid):
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)
    while q:
        x = q.popleft()
        for point, weight in matrix[x]:
            # 방문하지 않은 경우와
            if point not in visited:
                # 무게 제한이 되지 않은 경우에만 조건문 수행
                if weight >= mid:
                    visited.add(point)
                    q.append(point)
    return True if end in visited else False


while c_min <= c_max:
    mid = (c_min + c_max) // 2
    if bfs(mid):
        res = mid
        c_min = mid + 1
    else:
        c_max = mid - 1
# 중량의 최댓값을 구하는 프로그램
print(res)
