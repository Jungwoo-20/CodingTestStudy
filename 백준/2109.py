import sys
import heapq

n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    matrix.append([p, d])
matrix.sort(key=lambda x: (x[1]))
heap = []
for i in matrix:
    heapq.heappush(heap, i[0])
    if len(heap) > i[1]:
        heapq.heappop(heap)
print(sum(heap))