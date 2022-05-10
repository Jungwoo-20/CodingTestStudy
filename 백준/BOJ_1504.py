import sys, heapq

# 정점의 개수와 간선의 개수
N, E = map(int, sys.stdin.readline().split())
matrix = [[] for _ in range(N + 1)]
# 최대 거리
inf = sys.maxsize
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a].append([b, c])
    matrix[b].append([a, c])
# 두 개의 서로 다른 정점 번호
v1, v2 = map(int, sys.stdin.readline().split())


def solution(start):
    dist = [inf for _ in range(N + 1)]
    heap = []
    dist[start] = 0
    heapq.heappush(heap, [start, 0])
    while heap:
        point, weight = heapq.heappop(heap)
        for _point, _weight in matrix[point]:
            if dist[_point] > weight + _weight:
                dist[_point] = weight + _weight
                heapq.heappush(heap, [_point, weight + _weight])
    return dist


# 시작점, v1, v2에서 갈 수 있는 모든 경로의 비용을 탐색
res1 = solution(1)
res2 = solution(v1)
res3 = solution(v2)

# v1 -> v2 -> N 과 v2->v1->N의 거리 중 더 작은 거리를 탐색
# inf가 나오는 경우는 경로가 없기 때문에 조건에 의해 -1을 출력
cnt = min(res1[v1] + res2[v2] + res3[N], res1[v2] + res3[v1] + res2[N])
print(cnt if cnt < inf else -1)
