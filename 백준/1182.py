import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
matrix = list(map(int, sys.stdin.readline().split(' ')))
cnt = 0
for i in range(1,N+1):
    tmp = combinations(matrix,i)
    for j in tmp:
        if sum(j) == S:
            cnt+=1
print(cnt)