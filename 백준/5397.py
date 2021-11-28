import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    mun = sys.stdin.readline().rstrip()
    left = []
    right = []
    for i in mun:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))