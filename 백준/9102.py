import sys

n = int(sys.stdin.readline())
for _ in range(n):
    stk = 0
    mun = sys.stdin.readline().rstrip()
    mun = list(mun)
    for i in mun:
        if i == '(':
            stk += 1
        elif i == ')':
            stk -= 1
        if stk < 0:
            print('NO')
            break
    if stk > 0:
        print('NO')
    elif stk == 0:
        print('YES')
