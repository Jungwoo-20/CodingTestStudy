import sys

N = int(sys.stdin.readline())
parents = [i for i in range(N + 1)]


def find(x):
    if parents[x] != x:
        return find(parents[x])
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


for _ in range(N - 2):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)
flag = find(1)
for i in range(2, N + 1):
    if flag != find(i):
        print(flag, i)
        exit()
