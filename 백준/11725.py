import sys

sys.setrecursionlimit(10 ** 8)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)


def dfs(start, tree, parent):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i, tree, parent)


dfs(1, tree, parent)
for i in range(2, N + 1):
    print(parent[i])
