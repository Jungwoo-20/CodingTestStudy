from collections import deque

T = int(input())


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 2번 인덱스가 만나는 지점 0번 인덱스가 빨간색 화살표를 가리킬 수 있도록 접근
def solution(num, direc):
    # 현재 위치의 왼 우 방향 나사
    left = num - 1
    right = num + 1
    # 범위 체크
    if left >= 0:
        # 왼쪽 방문 구간 + 달라야 회전할 수 있음
        if not visited[left][2] and matrix[num][6] != matrix[left][2]:
            visited[left][2] = True
            visited[num][6] = True
            # 왼쪽 방향의 나사를 중심으로 또 다시 왼 오를 수행할려면 방향이 반대가 되어야함
            solution(left, -direc)
    # 범위 체크
    if right < 4:
        if not visited[right][6] and matrix[num][2] != matrix[right][6]:
            visited[right][6] = True
            visited[num][2] = True
            solution(right, -direc)
    # 시계방향(마지막 인덱스가 첫 번째로 와야함)
    if direc == 1:
        tmp = matrix[num].pop()
        matrix[num].insert(0, tmp)
        return
    # 반시계방향(첫 인덱스가 마지막에 와야함)
    else:
        tmp = matrix[num].popleft()
        matrix[num].append(tmp)
        return


def calculator():
    global res
    for i in range(4):
        # 1,2,4,8
        if matrix[i][0] == 1:
            res += 2 ** i
    return res


for test_case in range(1, T + 1):
    K = int(input())
    matrix = [deque(list(map(int, input().split()))) for _ in range(4)]
    res = 0
    for _ in range(K):
        # 자석 번호, 회전 방향
        num, direction = map(int, input().split())
        visited = [[False] * 7 for _ in range(4)]
        solution(num - 1, direction)
    print('#' + str(test_case) + ' ' + str(calculator()))
