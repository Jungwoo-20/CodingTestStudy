import heapq

INF = int(1e10)
matrix = [[]]


# 2차원 배열 생성
def init(n, fares):
    global matrix
    matrix = [[] for _ in range(n + 1)]
    for fa in fares:
        start, end, weight = fa[0], fa[1], fa[2]
        matrix[start].append([end, weight])
        matrix[end].append([start, weight])


def dijkstra(start, finish):
    global matrix
    # 이동 위치에 가장 작은 경로 저장 배열
    N = len(matrix)
    table = [INF for _ in range(1, N + 1)]
    # 시작 지점의 비용은 0
    table[start] = 0
    heap = [[start, 0]]
    while heap:
        end, weight = heapq.heappop(heap)
        # 현재 이동 거리 비용보다 이동하고자 하는 비용이 큰 경우 예외처리
        if table[end] < weight:
            continue
        # 현재 이동 위치에서 방문할 수 있는 곳 탐색
        for i in matrix[end]:
            _end, _weight = i[0], i[1]
            _weight += weight
            # 저장된 값보다 현재 이동할 때 비용이 적은 경우 업데이트
            if table[_end] > _weight:
                table[_end] = _weight
                heapq.heappush(heap, [_end, _weight])
    # 모든 경우를 방문할때 도착 지점의 비용을 반환
    return table[finish]


def solution(n, s, a, b, fares):
    answer = INF
    init(n, fares)
    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    return answer


# 프로그래머스 참고 코드(플로이드 와샬)
def solution(n, s, a, b, fares):
    d = [[20000001 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x - 1][y - 1] = c
        d[y - 1][x - 1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s - 1][i] + d[i][a - 1] + d[i][b - 1])
    return minv
