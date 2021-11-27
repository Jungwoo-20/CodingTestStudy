import sys

mun = sys.stdin.readline()
left = 0
res = 0
for i in range(len(mun)):
    if mun[i] == '(':
        left += 1
    elif mun[i] == ')':
        left -= 1
        if mun[i - 1] == '(':
            res += left
        else:
            res += 1
print(res)
