import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    matrix[start].append([end, weight])
start, end = map(int, sys.stdin.readline().split())

heap = []
dist = [sys.maxsize] * (N+1)
dist[start] = 0
heapq.heappush(heap, [start, 0])
while heap:
    _end, weight = heapq.heappop(heap)
    if weight > dist[_end]:
        continue
    for i, j in matrix[_end]:
        j += weight
        if j < dist[i]:
            dist[i] = j
            heapq.heappush(heap, [i, j])
print(dist[end])
