import sys
import heapq
from math import inf

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
matrix = [[] for _ in range(V + 1)]
dp = [inf] * (V + 1)
heap = []
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    matrix[u].append((v, w))
dp[K] = 0
heapq.heappush(heap, (0, K))
while heap:
    weight, now = heapq.heappop(heap)
    for i, j in matrix[now]:
        _weight = weight + j
        if _weight <= dp[i]:
            dp[i] = _weight
            heapq.heappush(heap, (_weight, i))
for i in dp[1:]:
    print(i if i != inf else 'INF')
