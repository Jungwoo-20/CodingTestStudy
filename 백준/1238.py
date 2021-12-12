import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

left = [[] for _ in range(N)]
ldist = [sys.maxsize] * N
right = [[] for _ in range(N)]
rdist = [sys.maxsize] * N
for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    left[start - 1].append([end - 1, weight])
    right[end - 1].append([start - 1, weight])


def heapQueue(X, matrix, dist):
    queue = []
    dist[X - 1] = 0
    heapq.heappush(queue, [X - 1, 0])
    while queue:
        point, weight = heapq.heappop(queue)
        if dist[point] < weight:
            continue
        for _point, _weight in matrix[point]:
            _weight += weight
            if _weight < dist[_point]:
                dist[_point] = _weight
                heapq.heappush(queue, [_point, _weight])
    return dist


res1 = heapQueue(X, left, ldist)
res2 = heapQueue(X, right, rdist)
result = 0
for i, j in zip(res1, res2):
    result = max(result, i + j)
print(result)
