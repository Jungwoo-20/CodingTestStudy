import sys
import heapq

n = int(sys.stdin.readline())
res = -1
heap = []
matrix = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
matrix.sort(key=lambda x: x[1])
d = int(sys.stdin.readline())

for start, end in matrix:
    tmp = end - d
    if tmp <= start:
        heapq.heappush(heap, start)
    while heap and heap[0] < tmp:
        heapq.heappop(heap)
    res = max(res, len(heap))
print(res)
