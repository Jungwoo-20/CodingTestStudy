from itertools import combinations
import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
members = [i for i in range(n)]
min_size = sys.maxsize

for mem in combinations(members, n // 2):
    start, link = 0, 0
    tmp = list(set(members) - set(mem))
    for r in combinations(mem, 2):
        start += matrix[r[0]][r[1]]
        start += matrix[r[1]][r[0]]
    for r in combinations(tmp, 2):
        link += matrix[r[0]][r[1]]
        link += matrix[r[1]][r[0]]
    if min_size > abs(start - link):
        min_size = abs(start - link)
print(min_size)
