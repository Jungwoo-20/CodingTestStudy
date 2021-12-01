# 시간 초과로 인한 pypy3로 제출
import sys

N, M = map(int, sys.stdin.readline().split())

matrix = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(matrix)
while left <= right:
    mid = (left + right) // 2
    res = 0
    for i in matrix:
        if i >= mid:
            res += i - mid
    if res >= M:
        left = mid + 1
    else:
        right = mid - 1
print(right)
