import sys

N = int(sys.stdin.readline())
matrix = list(map(int, sys.stdin.readline().split()))
matrix.sort()

flag = 1e10
res = [0] * 3

# 세 용액이므로 n-3까지 인덱스만 이
for i in range(N - 2):
    left, right = i + 1, N - 1

    while left < right:
        total = matrix[i] + matrix[left] + matrix[right]
        if abs(total) < abs(flag):
            res[0] = matrix[i]
            res[1] = matrix[left]
            res[2] = matrix[right]
            flag = total

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            # 0인 경우 이것보다 작아질 수 없으므로 출력 후 종료
            print(matrix[i], matrix[left], matrix[right])
            sys.exit()
# 0인 경우를 찾지 못하였으면 최소 상태인 값으로 출력
for k in range(3):
    print(res[k], end=' ')
