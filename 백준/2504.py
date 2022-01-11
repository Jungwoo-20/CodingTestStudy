import sys

mun = sys.stdin.readline().rstrip()
res = 1


def flag(mun0):
    stk = []
    for x in range(len(mun0)):
        if mun0[x] == '(' or mun0[x] == '[':
            stk.append(mun0[x])
        else:
            if mun0[x] == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                else:
                    return False
            else:
                if stk and stk[-1] == '[':
                    stk.pop()
                else:
                    return False
    return True


result = 0
chk = flag(mun)
if not chk:
    print(0)
else:
    stk1 = []
    for i in mun:
        if i == '(' or i == '[':
            stk1.append(i)
        elif i == ')':
            if stk1[-1] == '(':
                stk1[-1] = 2
            else:
                tmp = 0
                for j in range(len(stk1) - 1, -1, -1):
                    if stk1[-1] == '(':
                        stk1[-1] = tmp * 2
                        break
                    else:
                        tmp += stk1[j]
                        stk1 = stk1[:-1]
        elif i == ']':
            if stk1[-1] == '[':
                stk1[-1] = 3
            else:
                tmp = 0
                for j in range(len(stk1) - 1, -1, -1):
                    if stk1[-1] == '[':
                        stk1[-1] = tmp * 3
                        break
                    else:
                        tmp += stk1[j]
                        stk1 = stk1[:-1]
    print(sum(stk1))
