import sys


def pesudo(mun, left, right):
    while left < right:
        if mun[left] == mun[right]:
            left += 1
            right -= 1
        else:
            return 1
    return 0


def pelindrome(mun, left, right):
    while left < right:
        if mun[left] == mun[right]:
            left += 1
            right -= 1
        else:
            tmp1 = pesudo(mun, left + 1, right)
            tmp2 = pesudo(mun, left, right - 1)
            if tmp1 == 0 or tmp2 == 0:
                return 1
            else:
                return 2
    return 0


n = int(sys.stdin.readline())
for _ in range(n):
    mun = sys.stdin.readline().rstrip()
    res = pelindrome(mun, 0, len(mun) - 1)
    print(res)
