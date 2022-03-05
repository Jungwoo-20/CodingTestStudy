import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
queue = deque()
res = []
for i in range(N):
    tmp = lst[i]
    # 현재 tmp 보다 queue의 마지막이 더 큰경우 넣을 필요가 없다.(최소값을 맞추어야 하기 때문)
    while queue and queue[-1] > tmp:
        queue.pop()
    # 현재 값 삽입
    queue.append(tmp)
    # 윈도우 사이즈 보다 큰 경
    if i >= L and queue[0] == lst[i - L]:
        queue.popleft()
    res.append(queue[0])
print(*res)
