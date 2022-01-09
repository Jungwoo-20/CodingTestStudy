from collections import deque


def bfs(matrix, visited, start):
    cnt = 1
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        start = q.popleft()
        for i in matrix[start]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt


def solution(n, wires):
    answer = n
    matrix = [[] for _ in range(n + 1)]
    for start, end in wires:
        matrix[start].append(end)
        matrix[end].append(start)
    for start, end in wires:
        visited = [False] * (n + 1)
        visited[end] = True
        res = bfs(matrix, visited, start)
        if abs(res - (n - res)) < answer:
            answer = abs(res - (n - res))
    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
print(solution(n, wires))
