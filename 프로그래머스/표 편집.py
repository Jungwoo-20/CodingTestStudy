import heapq


def solution(n, k, cmd):
    answer = ['O'] * n
    # left = maxHeap, right = minHeap
    left, right, delete = [], [], []
    for i in range(n):
        if i < k:
            heapq.heappush(left, -i)
        else:
            heapq.heappush(right, i)
    k = 0
    for c in cmd:
        if c[0] == 'U':
            k -= int(c.split()[1])
        elif c[0] == 'D':
            k += int(c.split()[1])
        elif c[0] == 'C':
            if k >= 0:
                for i in range(k):
                    heapq.heappush(left, -heapq.heappop(right))
                delete.append(heapq.heappop(right))
                if not right:
                    heapq.heappush(right, -heapq.heappop(left))
            else:
                for i in range(-k - 1):
                    heapq.heappush(right, -heapq.heappop(left))
                delete.append(-heapq.heappop(left))
            k = 0
        else:
            n = delete.pop()
            if k < 0:
                for i in range(-k):
                    heapq.heappush(right, -heapq.heappop(left))
            else:
                for i in range(k):
                    heapq.heappush(left, -heapq.heappop(right))
            if right[0] < n:
                heapq.heappush(right, n)
            else:
                heapq.heappush(left, -n)
            k = 0
    for i in delete:
        answer[i] = 'X'
    answer = ''.join(answer)
    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
print(solution(n, k, cmd))
