import sys

N, M = map(int, sys.stdin.readline().split())

true_set = set(list(map(int, sys.stdin.readline().split()))[1:])

visited = [0] * M

party = []
for _ in range(M):
    party.append(list(map(int, sys.stdin.readline().split()))[1:])

for _ in range(M):
    for idx, part in enumerate(party):
        if true_set.intersection(set(part)):
            visited[idx-1] = 1
            true_set = true_set.union(part)
print(visited.count(0))
