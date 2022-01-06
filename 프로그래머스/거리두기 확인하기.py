from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(matrix, i, j, dist):
    queue = deque()
    visited = [[False] * 5 for _ in range(5)]
    queue.append((i, j, dist))
    while queue:
        x, y, d = queue.popleft()
        visited[x][y] = True
        for a in range(4):
            _x = x + dx[a]
            _y = y + dy[a]
            _d = d + 1
            if 0 <= _x < 5 and 0 <= _y < 5 and not visited[_x][_y]:
                visited[_x][_y] = True
                if matrix[_x][_y] == 'P':
                    if _d <= 2:
                        return False
                elif matrix[_x][_y] == 'O':
                    if _d == 1:
                        queue.append((_x, _y, _d))
    return True


def solution(places):
    answer = []

    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(place, i, j, 0):
                        flag = 0
        answer.append(flag)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
