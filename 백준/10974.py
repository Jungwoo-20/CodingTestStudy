import sys
from itertools import permutations

N = int(sys.stdin.readline())
matrix = [i for i in range(1,N+1)]
lst = permutations(matrix)
for i in lst:
    for j in i:
        print(j, end=' ')
    print()