import sys

N = int(sys.stdin.readline())

matrix = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
for i in range(1, len(matrix)):
    matrix[i] += matrix[i - 1]
# 누적 합
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    if start == 1:
        print(matrix[end])
    # 마지막 인덱스 값 - 시작 인덱스까지 더했던 값 = 시작부터 끝 인덱스까지의 합
    else:
        print(matrix[end] - matrix[start - 1])
