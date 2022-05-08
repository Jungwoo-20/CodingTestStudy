import sys
import heapq

tc = int(sys.stdin.readline())
inf = sys.maxsize


# 다익스트라 문제
def solution(start):
    # 다익스트라 비용 배열
    dist = [inf for _ in range(n + 1)]
    heap = []
    heapq.heappush(heap, [start, 0])
    # 시작 위치의 거리는 0으로 초기화
    dist[start] = 0
    while heap:
        _start, _weight = heapq.heappop(heap)
        for point, weight in matrix[_start]:
            if _weight + weight < dist[point]:
                dist[point] = _weight + weight
                heapq.heappush(heap, [point, _weight + weight])
    # 시작 위치부터 모든 의존 관계에 있는 컴퓨터를 방문한 후 결과를 출
    return dist


for _ in range(tc):
    # 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c
    n, d, c = map(int, sys.stdin.readline().split())
    matrix = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        # a가 b에 의존 -> b가 감염되면 연결된 정점은 전부 감염
        matrix[b].append([a, s])
    heap = solution(c)
    # 감염 컴퓨터 개수
    cnt = 0
    # 가장 오래 소요되는 시간
    time = 0
    for h in heap:
        # 방문하여 감염된 컴퓨터의 개수
        if h != inf:
            cnt += 1
            # 현재 시간보다 오래 걸린 시간이라면 업데이트
            if time < h:
                time = h
    # 총 감염되는 컴퓨터 수, 마지막 걸리는 시간
    res = [cnt, time]
    print(*res)
