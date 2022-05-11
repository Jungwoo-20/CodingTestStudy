import sys

N = int(sys.stdin.readline())
# [가능한 횟수, [만드는 방법에 포함된 수]]
matrix = [[0, []] for _ in range(N + 1)]
# 1로 만드는건 0번만에 가능, 포함된 수는 1
matrix[1][0] = 0
matrix[1][1] = [1]
# 1인 경우 그대로 출력하고 프로그램 종료
if N == 1:
    print(matrix[1][0])
    print(matrix[1][1][0])
    exit()
# 2부터 N까지 반복
for i in range(2, N + 1):
    # 1을 빼는 것은 모든 수에서 가능하기 때문에 별도의 조건문 불필요
    matrix[i][0] = matrix[i - 1][0] + 1
    matrix[i][1] = matrix[i - 1][1] + [i]

    # 3(2)으로 나누어 떨어지고 3(2)으로 나눈 가능한 횟수에 1을 더한 값보다 작은 경우 가능
    if i % 3 == 0 and matrix[i // 3][0] + 1 < matrix[i][0]:
        matrix[i][0] = matrix[i // 3][0] + 1
        matrix[i][1] = matrix[i // 3][1] + [i]
    if i % 2 == 0 and matrix[i // 2][0] + 1 < matrix[i][0]:
        matrix[i][0] = matrix[i // 2][0] + 1
        matrix[i][1] = matrix[i // 2][1] + [i]

print(matrix[N][0])
for i in matrix[N][1][::-1]:
    print(i, end=' ')
