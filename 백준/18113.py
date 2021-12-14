import sys

N, K, M = map(int, sys.stdin.readline().split())
matrix = []

for _ in range(N):
    matrix.append(int(sys.stdin.readline()))
start, end = 1, max(matrix)


def count(matrix, mid):
    cnt = 0
    for i in matrix:
        if i <= K:
            continue
        if i < (2 * K):
            i -= K
        else:
            i -= (2 * K)
        cnt += i // mid
    return cnt


res = 0
while start <= end:
    mid = (start + end) // 2
    if count(matrix, mid) >= M:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res if res else -1)
