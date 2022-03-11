import sys

N, M = map(int, sys.stdin.readline().split())
matrix = list(map(int, sys.stdin.readline().split()))
left, right = 0, 1
res = 0
# 왼쪽 포인터가 오른쪽 포인터보다 커지면 안됨
# 오른쪽 포인터가 배열의 길이보다 길어지면 안됨
while left <= right and right <= N:
    tmp = matrix[left:right]
    tmp = sum(tmp)
    # 값이 같아지게 되면 오른쪽 인덱스를 +=1
    if tmp == M:
        res += 1
        right += 1
    elif tmp > M:
        left += 1
    else:
        right += 1
print(res)
