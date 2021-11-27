import sys

key = sys.stdin.readline().rstrip()
key_len = len(key)
cnt = 0


def find_key(mun, key, key_len):
    for i in range(10):
        for j in range(key_len):
            nj = i + j
            if nj >= 10:
                nj -= 10
            if mun[nj] != key[j]:
                break
        else:
            return True
    return False


for _ in range(int(sys.stdin.readline())):
    if find_key(sys.stdin.readline().rstrip(), key, key_len):
        cnt += 1
print(cnt)
