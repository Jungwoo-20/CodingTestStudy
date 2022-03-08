import sys
import heapq

N = int(sys.stdin.readline())
res = []

for i in range(N):
    ma = list(map(int,sys.stdin.readline().split()))
    # heap이 비어 있는 경우
    if not res:
        # 해당 구간의 input정보를 heap에 저장
        for m in ma:
            # n만큼의 사이즈를 유지하는 것이 중요(핵심 포인트)
            heapq.heappush(res,m)
    else:
        for m in ma:
            # 입력값보다 가장 작은 수가 더 작을 경우
            if res[0] < m:
                # 해당 값을 넣어주고
                heapq.heappush(res, m)
                # res의 가장 작은 값을 pop하여 N길이를 유지
                heapq.heappop(res)
print(res[0])