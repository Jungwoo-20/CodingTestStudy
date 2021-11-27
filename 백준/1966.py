import sys
from collections import deque

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    que = deque(map(int, sys.stdin.readline().split()))
    cnt = 0
    while que:
        top = max(que)
        m -= 1
        tmp = que.popleft()
        if tmp != top:
            que.append(tmp)
            if m < 0:
                m = len(que) - 1
        else:
            cnt += 1
            if m == -1:
                print(cnt)
                break
