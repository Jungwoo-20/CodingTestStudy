import sys

TC = int(sys.stdin.readline())


def bellman_ford():
    global flag
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for edge, weight in matrix[j]:
                if dist[edge] > dist[j] + weight:
                    dist[edge] = dist[j] + weight
                    if i == N:
                        flag = False


for _ in range(TC):
    flag = True
    N, M, W = map(int, sys.stdin.readline().split())
    matrix = [[] for _ in range(N + 1)]
    dist = [sys.maxsize] * (N + 1)
    for i in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        matrix[S].append([E, T])
        matrix[E].append([S, T])
    for i in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        matrix[S].append([E, -T])
    bellman_ford()
    print('NO' if flag else 'YES')
